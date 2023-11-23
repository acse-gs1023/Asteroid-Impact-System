"""
This module contains the atmospheric entry solver class
for the Deep Impact project
"""
import os
import numpy as np
import pandas as pd


__all__ = ['Planet']


class Planet():
    """
    The class called Planet is initialised with constants appropriate
    for the given target planet, including the atmospheric density profile
    and other constants
    """

    def __init__(self, atmos_func='exponential',
                 atmos_filename=os.sep.join((os.path.dirname(__file__), '..',
                                             'resources',
                                             'AltitudeDensityTable.csv')),
                 Cd=1., Ch=0.1, Q=1e7, Cl=1e-3, alpha=0.3,
                 Rp=6371e3, g=9.81, H=8000., rho0=1.2):
        """
        Set up the initial parameters and constants for the target planet

        Parameters
        ----------
        atmos_func : string, optional
            Function which computes atmospheric density, rho, at altitude, z.
            Default is the exponential function rho = rho0 exp(-z/H).
            Options are 'exponential', 'tabular' and 'constant'

        atmos_filename : string, optional
            Name of the filename to use with the tabular atmos_func option

        Cd : float, optional
            The drag coefficient

        Ch : float, optional
            The heat transfer coefficient

        Q : float, optional
            The heat of ablation (J/kg)

        Cl : float, optional
            Lift coefficient

        alpha : float, optional
            Dispersion coefficient

        Rp : float, optional
            Planet radius (m)

        rho0 : float, optional
            Air density at zero altitude (kg/m^3)

        g : float, optional
            Surface gravity (m/s^2)

        H : float, optional
            Atmospheric scale height (m)

        """

        # Input constants
        self.Cd = Cd
        self.Ch = Ch
        self.Q = Q
        self.Cl = Cl
        self.alpha = alpha
        self.Rp = Rp
        self.g = g
        self.H = H
        self.rho0 = rho0
        self.atmos_filename = atmos_filename

        try:
            # set function to define atmoshperic density
            if atmos_func == 'exponential':
                self.rhoa = lambda z: rho0 * np.exp(-z / H)
            elif atmos_func == 'tabular':
                self.read_csv()
                self.rhoa = lambda x: self.linear_interpolate(x)
            elif atmos_func == 'constant':
                self.rhoa = lambda x: rho0
            else:
                raise NotImplementedError(
                    "atmos_func must be 'exponential', 'tabular' or 'constant'"
                    )
        except NotImplementedError:
            print("atmos_func {} not implemented yet.".format(atmos_func))
            print("Falling back to constant density atmosphere for now")
            self.rhoa = lambda x: rho0

    def rk4_step(self, f, y, t, dt):
        """RK4."""
        k1 = dt * f(t, y)
        k2 = dt * f(t + dt / 2, y + k1 / 2)
        k3 = dt * f(t + dt / 2, y + k2 / 2)
        k4 = dt * f(t + dt, y + k3)
        return y + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    def solve_atmospheric_entry(
        self,
        radius,
        velocity,
        density,
        strength,
        angle,
        init_altitude=100e3,
        dt=0.25,
        radians=False,
    ):
        if not radians:
            angle = np.radians(angle)

        def equations_of_motion(t, y):
            v, m, theta, z, x, r = y
            rho_a = self.rhoa(z)
            A = np.pi * r**2

            dvdt = (-self.Cd * rho_a * A * v**2) / (2 * m) + self.g * np.sin(theta)
            dmdt = (-self.Ch * rho_a * A * v**3) / (2 * self.Q)
            dthetadt = (
                (self.g * np.cos(theta)) / v
                - (self.Cl * rho_a * A * v) / (2 * m)
                - (v * np.cos(theta)) / (self.Rp + z)
            )
            dzdt = -v * np.sin(theta)
            dxdt = (v * np.cos(theta)) / (1 + z / self.Rp)
            drdt = (
                np.sqrt((7 / 2) * self.alpha * (rho_a / density)) * v
                if rho_a * v**2 > strength
                else 0
            )

            return np.array([dvdt, dmdt, dthetadt, dzdt, dxdt, drdt])

        y0 = np.array(
            [
                velocity,
                density * (4 / 3) * np.pi * radius**3,
                angle,
                init_altitude,
                0,
                radius,
            ]
        )
        t = 0
        results = []
        fragmented = False
        user_time_elapsed = 0.0  # Initialize the user-specified time elapsed counter

        while True:
            #
            dt_actual = min(dt, 0.05)
            y0 = self.rk4_step(equations_of_motion, y0, t, dt_actual)
            t += dt_actual
            user_time_elapsed += dt_actual

            if user_time_elapsed >= dt:
                results.append([t] + list(y0))
                user_time_elapsed = 0.0  # Reset the user-specified time elapsed counter

            if y0[0] <= 531:
                break

            ram_pressure = self.rhoa(y0[3]) * y0[0] ** 2
            if ram_pressure > strength:
                fragmented = True
            elif fragmented and ram_pressure <= strength:
                fragmented = False

        result_df = pd.DataFrame(
            results,
            columns=[
                "time",
                "velocity",
                "mass",
                "angle",
                "altitude",
                "distance",
                "radius",
            ],
        )

        # Converts the angle column in the result from radians to degrees
        result_df["angle"] = np.degrees(result_df["angle"])

        return result_df

    def calculate_energy(self, result):
    # Calculate the kinetic energy at each step
        kinetic_energy = 0.5 * result['mass'] * result['velocity']**2

    # Convert kinetic energy from Joules to kilotons of TNT (1 kt TNT = 4.184e12 Joules)
        kinetic_energy_kt = kinetic_energy / 4.184e12

    # Calculate the energy change between successive steps
        energy_diff = np.diff(kinetic_energy_kt, prepend=kinetic_energy_kt[0])

    # Calculate the altitude difference between successive steps
        altitude_diff = np.diff(result['altitude'], prepend=result['altitude'][0])

    # Calculate dedz (change in energy per kilometer of altitude)
    # Note: Convert altitude change from meters to kilometers for correct units
    # Avoid division by zero by replacing zeros with a small number
        altitude_diff[altitude_diff == 0] = 1e-6
        dedz = energy_diff / (altitude_diff / 1000)

    # Update or create the 'dedz' column
        result['dedz'] = dedz

        return result


    def analyse_outcome(self, result):
        """
        Inspect a pre-found solution to calculate the impact and airburst stats

        Parameters
        ----------
        result : DataFrame
            pandas dataframe with velocity, mass, angle, altitude, horizontal
            distance, radius and dedz as a function of time

        Returns
        -------
        outcome : Dict
            dictionary with details of the impact event, which should contain
            the key:
                ``outcome`` (which should contain one of the
                following strings: ``Airburst`` or ``Cratering``),
            as well as the following 4 keys:
                ``burst_peak_dedz``, ``burst_altitude``,
                ``burst_distance``, ``burst_energy``
        """

        outcome = {'outcome': 'Unknown',
                'burst_peak_dedz': 0.,
                'burst_altitude': 0.,
                'burst_distance': 0.,
                'burst_energy': 0.}
        # Check if the DataFrame is empty
        if result.empty:
            return outcome

        # Find the index of the maximum energy deposition rate
        max_dedz_idx = result['dedz'].idxmax()
        max_dedz = result.loc[max_dedz_idx, 'dedz']

        # Check if the max energy deposition occurs at an altitude above 0
        max_dedz_altitude = result.loc[max_dedz_idx, 'altitude']
        if max_dedz_altitude > 0:
            outcome['outcome'] = 'Airburst'
            outcome['burst_peak_dedz'] = max_dedz
            outcome['burst_altitude'] = max_dedz_altitude
            outcome['burst_distance'] = result.loc[max_dedz_idx, 'distance']

            # Calculate the kinetic energy loss from initial altitude to burst altitude
            initial_kinetic_energy = 0.5 * result.loc[0, 'mass'] * result.loc[0, 'velocity']**2
            burst_kinetic_energy = 0.5 * result.loc[max_dedz_idx, 'mass'] * result.loc[max_dedz_idx, 'velocity']**2
            energy_loss = initial_kinetic_energy - burst_kinetic_energy

            # Convert energy loss to kilotons (1 kt = 4.184e12 joules)
            outcome['burst_energy'] = energy_loss / 4.184e12
        else:
            outcome['outcome'] = 'Cratering'
            # Additional details for cratering can be added based on specific criteria

        return outcome
    
    def read_csv(self):
        self.altitudes = []
        self.densities = []
        with open(self.atmos_filename, 'r') as file:
            next(file)  # Skip the header line
            for line in file:
                if line.strip():  # Check if line is not empty
                    parts = line.split()
                    self.altitudes.append(float(parts[0]))  # Altitude value
                    self.densities.append(float(parts[1]))  # Density value


    def linear_interpolate(self, x):
        for i in range(len(self.altitudes) - 1):
            if self.altitudes[i] <= x <= self.altitudes[i + 1]:
                return self.densities[i] + (self.densities[i + 1] - self.densities[i]) * \
                       (x - self.altitudes[i]) / (self.altitudes[i + 1] - self.altitudes[i])
        return None  # Return None or handle extrapolation
