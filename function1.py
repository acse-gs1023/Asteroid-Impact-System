# import numpy as np
# import pandas as pd
# from deepimpact import Planet

# def test_planet():
#     data = np.load('tests/scenario.npz')

#     # Provide a default value for strength if it's not in the file
#     default_strength = 1e5  # Example default value, adjust as needed

#     radius = data['radius'][0] if data['radius'].size == 1 else data['radius']
# # Extract the first value from the velocity array
#     velocity = data['velocity'][0]

#     angle = data['angle'][0] if data['angle'].size == 1 else data['angle']
#     init_altitude = data['altitude'][0] if data['altitude'].size == 1 else data['altitude']

#     # Assuming mass and radius are provided to calculate density
#     density = data['mass'][0] / ((4/3) * np.pi * radius**3) if data['mass'].size == 1 else data['mass'] / ((4/3) * np.pi * radius**3)
#     strength = data.get('strength', default_strength)

#     dt = 0.05  # Set your desired time step
#     radians = False  # Set based on how angle is provided

#     planet = Planet()

#     result = planet.solve_atmospheric_entry(
#         radius,
#         velocity,
#         density,
#         strength,
#         angle,
#         init_altitude,
#         dt,
#         radians
#     )

#     print(result.head())

# if __name__ == "__main__":
#     test_planet()


import numpy as np
import pandas as pd
from deepimpact import Planet


def test_planet():
    data = np.load("tests/scenario.npz")

    # Provide a default value for strength if it's not in the file
    default_strength = 1e5  # Example default value, adjust as needed

    # Ensure that radius, velocity, angle, and init_altitude are scalars
    radius = data["radius"][0] if "radius" in data and data["radius"].size else None
    velocity = (
        data["velocity"][0] if "velocity" in data and data["velocity"].size else None
    )
    angle = data["angle"][0] if "angle" in data and data["angle"].size else None
    init_altitude = (
        data["altitude"][0] if "altitude" in data and data["altitude"].size else None
    )

    # Assuming mass and radius are provided to calculate density
    density = (
        data["mass"][0] / ((4 / 3) * np.pi * radius**3)
        if "mass" in data and data["mass"].size
        else None
    )
    strength = data.get("strength", default_strength)

    dt = 0.25  # Set your desired time step
    radians = False  # Set based on how angle is provided

    planet = Planet()

    result = planet.solve_atmospheric_entry(
        radius, velocity, density, strength, angle, init_altitude, dt, radians
    )

    print(result)


if __name__ == "__main__":
    data = np.load("tests/scenario.npz")
    # default_strength = 1e5
    # density = (
    #     data["mass"][0] / ((4 / 3) * np.pi * data["radius"] ** 3)
    #     if "mass" in data and data["mass"].size
    #     else None
    # )
    # print("*****************")
    # # 获取NPZ文件中的所有键
    # keys = data.files

    df = pd.DataFrame()
    for key in data.files:
        df[key] = data[key]
    print(df)
    # planet = Planet()
    # strength = data.get("strength", default_strength)
    # result = planet.solve_atmospheric_entry(
    #     data["radius"][0],
    #     data["velocity"][0],
    #     density,
    #     strength,
    #     data["angle"][0],
    #     data["altitude"][0],
    #     0.05,
    #     False,
    # )
    # test_planet()


# def test_calculate_energy():
#     # Create a sample DataFrame
#     sample_data = {
#         'velocity': [19000, 18000, 17000],  # Sample velocity data
#         'mass': [1000, 950, 900],           # Sample mass data
#         'radius': [5, 5, 5],                # Constant radius
#         'angle': [45, 45, 45],              # Constant angle
#         'altitude': [100000, 95000, 90000], # Decreasing altitude
#         'distance': [0, 1000, 2000]         # Sample horizontal distance
#     }
#     sample_df = pd.DataFrame(sample_data)

#     # Create an instance of Planet
#     planet = Planet()

#     # Call the calculate_energy method
#     result_with_energy = planet.calculate_energy(sample_df)

#     # Check the returned DataFrame
#     print(result_with_energy)

#     # Additional checks can be made here to validate the 'dedz' values


# if __name__ == "__main__":
#     test_calculate_energy()
def test_scenario(planet):
    inputs = {
        "radius": 35.0,
        "angle": 45.0,
        "strength": 1e7,
        "density": 3000.0,
        "velocity": 19e3,
    }

    #
    radians = np.radians(inputs["angle"])

    #  solve_atmospheric_entry
    result_df = planet.solve_atmospheric_entry(
        radius=inputs["radius"],
        velocity=inputs["velocity"],
        density=inputs["density"],
        strength=inputs["strength"],
        angle=radians,
        radians=True,  #
    )

    return result_df


planet_instance = Planet()

test_result = test_scenario(planet_instance)
print(test_result)
