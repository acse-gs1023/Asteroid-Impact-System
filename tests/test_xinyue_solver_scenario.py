from collections import OrderedDict
import pandas as pd
import numpy as np
import os
import sys
import pytest

BASE_PATH = os.path.dirname(__file__)
sys.path.append(os.path.dirname(BASE_PATH))
from pytest import fixture, mark


# Use pytest fixtures to generate objects we know we'll reuse.
# This makes sure tests run quickly

@fixture(scope='module')
def deepimpact():
    import deepimpact
    return deepimpact


@fixture(scope='module')
def planet(deepimpact):
    return deepimpact.Planet()


@fixture(scope='module')
def loc(deepimpact):
    return deepimpact.GeospatialLocator()


@fixture(scope='module')
def result(planet):
    input = {'radius': 1.,
             'velocity': 2.0e4,
             'density': 3000.,
             'strength': 1e5,
             'angle': 30.0,
             'init_altitude': 10000.0,
             }

    result = planet.solve_atmospheric_entry(**input)

    return result


@fixture(scope='module')
def outcome(planet, result):
    outcome = planet.analyse_outcome(result=result)
    return outcome


def test_import(deepimpact):
    assert deepimpact


def test_planet_signature(deepimpact):
    inputs = OrderedDict(atmos_func='exponential',
                         atmos_filename=None,
                         Cd=1., Ch=0.1, Q=1e7, Cl=1e-3,
                         alpha=0.3, Rp=6371e3,
                         g=9.81, H=8000., rho0=1.2)

    # call by keyword
    _ = deepimpact.Planet(**inputs)

    # call by position
    _ = deepimpact.Planet(*inputs.values())


def test_attributes(planet):
    for key in ('Cd', 'Ch', 'Q', 'Cl',
                'alpha', 'Rp', 'g', 'H', 'rho0'):
        assert hasattr(planet, key)


def test_atmos_filename(planet):

    assert os.path.isfile(planet.atmos_filename)


def test_solve_atmospheric_entry(result):

    assert type(result) is pd.DataFrame

    for key in ('velocity', 'mass', 'angle', 'altitude',
                'distance', 'radius', 'time'):
        assert key in result.columns

    # Verify that the result is a pandas DataFrame
    assert isinstance(result, pd.DataFrame), "Result should be a pandas DataFrame"
    # Check that numeric columns contain appropriate data types
    for column in ['velocity', 'mass', 'angle', 'altitude', 'distance', 'radius']:
        assert pd.api.types.is_numeric_dtype(result[column]), f"Column '{column}' should have a numeric data type"

    # Check for non-negative values where applicable (e.g., mass, radius)
    for column in ['mass', 'radius']:
        # assert (result[column] >= 0).all(), f"Column '{column}' should contain only non-negative values"

    # Check that the time column is sorted, if it should be
        assert (result['time'].sort_values() == result['time']).all(), "Time column should be sorted"


def load_expected_data():
    # Load the expected data from scenario.npz
    data = np.load('scenario.npz')  # change this to your own path
    df = pd.DataFrame()
    for key in data.files:
        df[key] =  data[key]
    return df


def test_calculate_energy(planet, result):

    energy = planet.calculate_energy(result=result)

    assert type(energy) is pd.DataFrame

    for key in ('velocity', 'mass', 'angle', 'altitude',
                'distance', 'radius', 'time', 'dedz'):
        assert key in energy.columns

   
    # Check for non-negative values in certain columns
    assert energy['velocity'].ge(0).all()
    assert energy['mass'].ge(0).all()
    for column in ['velocity', 'mass', 'distance', 'radius']:
        assert energy[column].ge(0).all()





def test_analyse_outcome(outcome):
    print(outcome)

    assert type(outcome) is dict
    

    for key in ('outcome', 'burst_peak_dedz', 'burst_altitude',
                'burst_distance', 'burst_energy'):
        assert key in outcome.keys()


    # Check the types of the values
    assert isinstance(outcome['outcome'], str), "The 'outcome' should be a string"
    assert isinstance(outcome['burst_peak_dedz'], (int, float)), "The 'burst_peak_dedz' should be a number"
    assert isinstance(outcome['burst_altitude'], (int, float)), "The 'burst_altitude' should be a number"
    assert isinstance(outcome['burst_distance'], (int, float)), "The 'burst_distance' should be a number"
    assert isinstance(outcome['burst_energy'], (int, float)), "The 'burst_energy' should be a number"

    assert outcome['outcome'] in ['Airburst', 'Cratering'], "The 'outcome' should be either 'Airburst' or 'Cratering'"
    assert outcome['burst_peak_dedz'] >= 0, "The 'burst_peak_dedz' should be non-negative"
    assert outcome['burst_altitude'] >= 0, "The 'burst_altitude' should be non-negative"
    assert outcome['burst_distance'] >= 0, "The 'burst_distance' should be non-negative"
    assert outcome['burst_energy'] >= 0, "The 'burst_energy' should be positive"
    # Consistency Tests: Check that the data within the outcome is consistent. For example, if a larger burst_energy should correlate with a larger burst_peak_dedz
    if 'burst_energy' in outcome and 'burst_peak_dedz' in outcome:
        assert outcome['burst_energy'] >= outcome['burst_peak_dedz'], "The 'burst_energy' should be greater than or equal to 'burst_peak_dedz'"



def load_expected_data():
    # Load the expected data from scenario.npz
    data = np.load('scenario.npz')  # change this to your own path
    df = pd.DataFrame()
    for key in data.files:
        df[key] =  data[key]
    return df



def test_scenario(planet):
    inputs = {'radius': 35.,
              'angle': 45.,
              'strength': 1e7,
              'density': 3000.,
              'velocity': 19e3}


    # Run the simulation
    result = planet.solve_atmospheric_entry(**inputs)

    assert type(result) is pd.DataFrame
    for key in ('velocity', 'mass', 'angle', 'altitude',
            'distance', 'radius', 'time'):
     assert key in result.columns

    # Load the expected scenario data
    expected_data = load_expected_data()

    # Compare the result with expected data
    # This assumes both result and expected_data are DataFrames with the same structure
    assert isinstance(result, pd.DataFrame), "Result should be a pandas DataFrame"
    num_rows_to_compare = 20  #
    for column in expected_data.columns:
        if column not in inputs:  # Skip the columns that are part of the inputs
            assert column in result.columns, f"Column '{column}' not found in result DataFrame"
            assert np.allclose(result[column].iloc[:num_rows_to_compare], 
                               expected_data[column].iloc[:num_rows_to_compare], 
                               atol=1), f"{column} data does not match expected results in the first {num_rows_to_compare} rows"




    # Get the last row of expected_data
    last_row_expected = expected_data.iloc[-1]

    # Find the closest row in result to time=10.75 using np.isclose
    time_10_75_mask = np.isclose(result['time'], 10.75, atol=1)
    assert time_10_75_mask.any(), "No matching time found for 10.75 in result"
    result_at_10_75 = result[time_10_75_mask].iloc[0]

    # Check if the closest row in result at time=10.75 matches the values of the last row of expected_data
    for column in expected_data.columns:
        if column not in inputs:  # Skip the columns that are part of the inputs
            assert np.isclose(result_at_10_75[column], last_row_expected[column], atol=1), f"{column} at time 10.75 does not match expected value from scenario.npz"



def test_damage_zones(deepimpact):

    outcome = {'burst_peak_dedz': 1000.,
               'burst_altitude': 9000.,
               'burst_distance': 90000.,
               'burst_energy': 6000.,
               'outcome': 'Airburst'}

    blat, blon, damrad = deepimpact.damage_zones(outcome, 55.0, 0.,
                                                 135., [27e3, 43e3])

    assert type(blat) is float
    assert type(blon) is float
    assert type(damrad) is list
    assert len(damrad) == 2


@mark.xfail
def test_great_circle_distance(deepimpact):

    pnts1 = np.array([[54.0, 0.0], [55.0, 1.0], [54.2, -3.0]])
    pnts2 = np.array([[55.0, 1.0], [56.0, -2.1], [54.001, -0.003]])

    data = np.array([[1.28580537e+05, 2.59579735e+05, 2.25409117e+02],
                    [0.00000000e+00, 2.24656571e+05, 1.28581437e+05],
                    [2.72529953e+05, 2.08175028e+05, 1.96640630e+05]])

    dist = deepimpact.great_circle_distance(pnts1, pnts2)

    assert np.allclose(data, dist, rtol=1.0e-4)



def test_locator_postcodes(loc):

    latlon = (52.2074, 0.1170)

    result = loc.get_postcodes_by_radius(latlon, [0.2e3, 0.1e3])

    assert type(result) is list
    if len(result) > 0:
        for element in result:
            assert type(element) is list



if __name__  == '__main__':
    pytest.main([__file__])