#!/usr/bin/env python3


import math
import sys


def calculate_distance(
        point1: tuple[int, int, int],
        point2: tuple[int, int, int]) -> float:
    """Return Euclidean distance between two 3D coordinate tuples."""
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    result = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return result


def ft_coordinate_system() -> None:
    """Parse a coordinate tuple and demonstrate tuple operations."""
    print("=== Game Coordinate System ===")
    print()

    position = (10, 20, 5)
    print(f"Position created: {position}")
    distance = calculate_distance((0, 0, 0), position)
    print(f"Distance between (0, 0, 0) and {position}: {distance:.2f}")
    print()

    try:
        coord_input = sys.argv[1]
    except IndexError:
        coord_input = "3,4,0"
    coordinates = coord_input.split(",")
    parsed_position: tuple[int, int, int] | None = None

    print(f"Parsing coordinates: \"{coord_input}\"")
    try:
        x_str, y_str, z_str = coordinates
    except ValueError:
        print("Error: Expected 3 coordinates (x, y, z).")
    else:
        try:
            parsed_position = (int(x_str), int(y_str), int(z_str))
            print(f"Parsed position: {parsed_position}")
            distance = calculate_distance((0, 0, 0), parsed_position)
            print(
                f"Distance between (0, 0, 0) and "
                f"{parsed_position}: {distance:.2f}"
            )
        except ValueError as e:
            print(f"Parsing invalid coordinates: \"{coord_input}\"")
            print(f"Error parsing coordinates: {e}")
            error_message, = e.args
            error_args = (error_message,)
            print(f"Error details - Type: ValueError, Args: {error_args}")

    invalid_input = "abc,def,ghi"
    if coord_input != invalid_input:
        print(f"Parsing invalid coordinates: \"{invalid_input}\"")
        invalid_coordinates = invalid_input.split(",")
        try:
            _ = (
                int(invalid_coordinates[0]),
                int(invalid_coordinates[1]),
                int(invalid_coordinates[2]),
            )
        except ValueError as e:
            print(f"Error parsing coordinates: {e}")
            error_message, = e.args
            error_args = (error_message,)
            print(f"Error details - Type: ValueError, Args: {error_args}")
    print()

    if parsed_position is not None:
        print("Unpacking demonstration:")
        x, y, z = parsed_position
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    ft_coordinate_system()
