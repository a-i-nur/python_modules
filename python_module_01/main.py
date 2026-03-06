#!/usr/bin/env python3

"""
Helper file for CodeCultivation module 01.

Run from module root:
    python3 main.py
"""

from importlib import util
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent

EXERCISE_FILES = {
    "ft_garden_intro": ROOT_DIR / "ex0" / "ft_garden_intro.py",
    "ft_garden_data": ROOT_DIR / "ex1" / "ft_garden_data.py",
    "ft_plant_growth": ROOT_DIR / "ex2" / "ft_plant_growth.py",
    "ft_plant_factory": ROOT_DIR / "ex3" / "ft_plant_factory.py",
    "ft_garden_security": ROOT_DIR / "ex4" / "ft_garden_security.py",
    "ft_plant_types": ROOT_DIR / "ex5" / "ft_plant_types.py",
    "ft_garden_analytics": ROOT_DIR / "ex6" / "ft_garden_analytics.py",
}


def load_module_from_file(function_name: str):
    """Load a Python module from an exercise file path."""
    file_path = EXERCISE_FILES[function_name]
    if not file_path.exists():
        raise ImportError(f"File not found: {file_path}")

    module_name = f"test_{function_name}"
    spec = util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load spec from: {file_path}")

    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_ft_exercise(exercise_file_name: str) -> None:
    """Run one exercise function by exact function name."""
    print(f"\n=== Testing {exercise_file_name} ===")

    try:
        ft_module = load_module_from_file(exercise_file_name)
        ft_function = getattr(ft_module, exercise_file_name)
        ft_function()
    except ImportError as error:
        print(f"Could not load exercise file: {error}")
    except AttributeError:
        print(f"Could not find function {exercise_file_name}() in your file")
        print(f"Make sure you have: def {exercise_file_name}()")
    except TypeError as error:
        print(f"Type error: {error}")
        print("Check your function parameters and types")
    except Exception as error:
        print(f"Error running your function: {error}")
        print("Check your code for syntax/runtime errors")


def main() -> None:
    """Run test menu for all exercises in module 01."""
    print("CodeCultivation - Module 01 tester")
    print("This helper tests ex0 to ex6.\n")
    print("0 - ft_garden_intro")
    print("1 - ft_garden_data")
    print("2 - ft_plant_growth")
    print("3 - ft_plant_factory")
    print("4 - ft_garden_security")
    print("5 - ft_plant_types")
    print("6 - ft_garden_analytics")
    print("a - test all")
    print()

    choice = input("Enter your choice: ").strip().lower()

    if choice == "0":
        test_ft_exercise("ft_garden_intro")
    elif choice == "1":
        test_ft_exercise("ft_garden_data")
    elif choice == "2":
        test_ft_exercise("ft_plant_growth")
    elif choice == "3":
        test_ft_exercise("ft_plant_factory")
    elif choice == "4":
        test_ft_exercise("ft_garden_security")
    elif choice == "5":
        test_ft_exercise("ft_plant_types")
    elif choice == "6":
        test_ft_exercise("ft_garden_analytics")
    elif choice == "a":
        for function_name in EXERCISE_FILES:
            test_ft_exercise(function_name)
    else:
        print("Invalid choice. Use 0-6 or a.")


if __name__ == "__main__":
    main()
