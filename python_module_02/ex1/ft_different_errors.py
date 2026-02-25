#!/usr/bin/env python3

def garden_operations() -> None:
    print("Testing ValueError...")
    try:
        int("plant")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    print("Testing ZeroDivisionError...")
    try:
        _ = 42 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    print("Testing FileNotFoundError...")
    file = None
    try:
        file = open("missing.txt", "r")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")
    finally:
        if file is not None:
            file.close()

    print("Testing KeyError...")
    try:
        plants = {"rose": 1, "tulip": 2}
        _ = plants["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    print("Testing multiple errors together...")
    try:
        _ = (100 / 0) + int("abc")
    except (ZeroDivisionError, ValueError):
        print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
