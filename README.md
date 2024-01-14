# ACS-1-deepimpact

## Problem Statement
Asteroids entering Earth’s atmosphere are subject to extreme drag forces that decelerate, heat and disrupt the space rocks. Stimulate the path of asteroid entering the earth's atmosphere and the zero point of impact. Further calculate the impacted radius and population by the asteroid impact.

For more details, refer to `ProjectDescription.ipynb`, `AirburstSolver.ipynb` and `DamageMapper.ipynb`.


This is a very brief Readme to get a basic understanding to how to install and run the tool you will develop.

## Installation

To install the module and any pre-requisites, from the base directory run
```
pip install -r requirements.txt
pip install -e .
```  

## Downloading postcode data

To download the postcode data
```
python download_data.py
```

## Automated testing

To run the pytest test suite, from the base directory run
```
pytest tests/
```


## Documentation

To generate the documentation (in html format)
```
python -m sphinx docs html
```

See the `docs` directory for the documentation,

## Example usage

For example usage see `example.py` in the examples folder:
```
python examples/example.py
```

## More information

For more information on the project specfication, see the python notebooks: `ProjectDescription.ipynb`, `AirburstSolver.ipynb` and `DamageMapper.ipynb`.

