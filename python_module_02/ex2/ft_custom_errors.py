#!/usr/bin/env python3

class GardenError(Exception):
    """A basic error for garden problems."""
    pass


class PlantError(GardenError):
    """For problems with plants (inherits from GardenError)"""
    pass


class WaterError(GardenError):
    """For problems with watering (inherits from GardenError)"""
    pass


def tomato_care() -> None:
    raise PlantError("The tomato plant is wilting!")


def water_tank() -> None:
    raise WaterError("Not enough water in the tank!")


def garden_life() -> None:
    print("Testing PlantError...")
    try:
        tomato_care()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        water_tank()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    try:
        tomato_care()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        water_tank()
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    garden_life()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_custom_errors()
