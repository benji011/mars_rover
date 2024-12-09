import sys
from models import Coordinates, RoverPosition
from exceptions import UnknownCommandError

command_mapper = {
    "N": {"L": "W", "R": "E", "F": Coordinates(0, 1)},
    "E": {"L": "N", "R": "S", "F": Coordinates(1, 0)},
    "S": {"L": "E", "R": "W", "F": Coordinates(0, -1)},
    "W": {"L": "S", "R": "N", "F": Coordinates(-1, 0)},
}


def parse_rover_position(rover_state: str) -> RoverPosition:
    parts = rover_state.strip("()").split(", ")
    x, y, direction = map(str.strip, parts)
    x, y = map(int, [x, y])
    return RoverPosition(x, y, direction)


def move_rover_forward(rover: RoverPosition, command: str) -> RoverPosition:
    # Depending on the direction of the rover, it's version of moving forwards
    # is relative to it. e.g. If it is facing E, then it must move 1 by
    # 1 space, which is represented as "x -> x + 1"
    movement = command_mapper[rover.direction][command]
    return RoverPosition(
        x=rover.x + movement.x,
        y=rover.y + movement.y,
        direction=rover.direction,
    )


def move_rover_90_degrees_l_or_r(rover: RoverPosition, command: str) -> RoverPosition:
    # The x & y values don't change for the rover, but the direction does. We simply
    # just override it's direction using a mapper and return as a new RoverPosition object.
    return RoverPosition(
        x=rover.x,
        y=rover.y,
        direction=command_mapper[rover.direction][command],
    )


def unknown_command(rover: RoverPosition, command: str):
    raise UnknownCommandError(f"{rover} received an unknown command {command}")


def execute_mission_instructions(
    rover: RoverPosition, instructions: str, boundaries: Coordinates
) -> str:
    try:
        last_valid_rover_position = ""
        valid_commands = {
            "F": move_rover_forward,
            "L": move_rover_90_degrees_l_or_r,
            "R": move_rover_90_degrees_l_or_r,
        }
        for command in instructions:
            # Create a copied state of the rover before it was moved with a command
            # from the instructions. If it's gone off the grid after execution then
            # we know that it will appear as LOST
            last_valid_rover_position = rover
            if command != "\n":
                rover = valid_commands.get(command, unknown_command)(
                    rover=rover, command=command
                )

                # Check the boundaries of the rover to see if it's not gone
                # over the grid m x n. If it has, then we've lost its position.
                if rover.x < 0 or rover.x > boundaries.x:
                    return f"{last_valid_rover_position} LOST"
                if rover.y < 0 or rover.y > boundaries.y:
                    return f"{last_valid_rover_position} LOST"

    # TODO: Set up actual logging here
    except UnknownCommandError as e:
        print(e)

    return rover


if __name__ == "__main__":
    file_from_cli = sys.argv[1]
    with open(file_from_cli, "r") as file:
        # The first line in the input is used to create the size of the grid
        first_line = file.readline()
        x, y = map(int, first_line.split())
        world_grid = Coordinates(x, y)

        # After getting the world grid, we need to parse the initial state of each rover and
        # the directions for which the rover needs to orientate to.
        robots = file.readlines()
        for robot in robots:
            position, instructions = robot.split(") ")
            rover = parse_rover_position(position)
            final_position = execute_mission_instructions(
                rover=rover, instructions=instructions, boundaries=world_grid
            )
            print(final_position)
