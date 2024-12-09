## Setup

The app uses `Python 3.10.5`.

It doesn't use any other dependencies other than Pythons built-in modules, but just incase to ensure nothing is conflicting please set your virtual environment by [installing pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation) and then run the below commands:

```shell
pyenv virtualenv multiverse-venv
pyenv local multiverse-venv
```

## Running the app

```shell
❯ python main.py input_1.txt
(4, 4, E)
(0, 4, W) LOST
```

## Running tests

```shell
❯ python -m unittest test_rover.py
```

# Improvements to be considered

Below are a few things I've listed that needs improvement, but I don't have time for as per instructions I kept this under 2-3 hours.

1. More error handling, particularly input validation
2. Needs docstrings
3. Set up logger to properly log out messages based on category. e.g. info, debug, warning, errors etc
4. More modules to separate concerns. Currently doesn't follow DRY or SOLID very well due to time constraints
