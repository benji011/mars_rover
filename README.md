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
