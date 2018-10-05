# PyTest tests for Chicken Attack game

Unit and integration tests for the Chicken Attack AI game. Only tests base game classes.

## How to use

These tests run using the Python 2 version of pytest and also work with pytest-cov coverage package.

Install pytest and pytest-cov like so:

```
pip install --user pytest 
pip install --user pytest-cov
```

Run the following from the base repo of this git repository to run the tests:

```
python -m pytest tests/
```

Running with pytest-cov generates an HTML report of test coverage:

```
python -m py.test --cov-report html:cov_html --cov=. tests/
```

## Example Test Run

```
~/git/chickenAttack$ python -m pytest tests/
================= test session starts ==================
platform linux2 -- Python 2.7.15rc1, pytest-3.8.2, py-1.
6.0, pluggy-0.7.1
rootdir: ~/git/chickenAttack, inifile:
plugins: cov-2.6.0
collected 13 items

tests/test_actions.py .....                      [ 38%]
tests/test_map.py .....                          [ 76%]
tests/test_player_integration.py ...             [100%]

============== 13 passed in 0.33 seconds ===============
```