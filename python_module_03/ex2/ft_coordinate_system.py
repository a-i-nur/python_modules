#!/bin/usr/env python3
"""
Exercise 2: Coordinate System.

Collection theory: tuples are immutable sequences used for fixed-size data,
such as coordinates. They are hashable (when elements are hashable) and
support unpacking, which improves readability in geometry calculations.
"""

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

    coord_input = sys.argv[1]

    if (len(sys.argv) != 2):
        print(f"Usage: {sys.argv[0]} <x, y, z>")
        return

    coordinates = sys.argv[1].split(',')
    if len(coordinates) != 3:
        print(
            f"Error: Expected 3 coordinates (x, y, z), "
            f"got {len(coordinates)}.")
        return

    try:
        print(f"Parsing coordinates: \"{coord_input}\"")
        position = tuple(int(axis) for axis in coordinates)
        print(f"Parsed position: {position}")
    except ValueError as e:
        print(f"Parsing invalid coordinates: \"{sys.argv[1]}\"")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        return

    distance = calculate_distance((0, 0, 0), position)
    print(f"Distance between (0, 0, 0) and {position}: {distance:.2f}")
    print()

    print("Unpacking demonstration:")
    x, y, z = position
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    ft_coordinate_system()
