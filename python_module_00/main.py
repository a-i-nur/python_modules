#!/usr/bin/env python3

"""
Helper file for Growing Code.

This file helps you test your exercises easily.
Run it from python_module_00 root:
    python3 main.py
"""

from importlib import util
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent

EXERCISE_FILES = {
    "ft_hello_garden": ROOT_DIR / "ex0" / "ft_hello_garden.py",
    "ft_plot_area": ROOT_DIR / "ex1" / "ft_plot_area.py",
    "ft_harvest_total": ROOT_DIR / "ex2" / "ft_harvest_total.py",
    "ft_plant_age": ROOT_DIR / "ex3" / "ft_plant_age.py",
    "ft_water_reminder": ROOT_DIR / "ex4" / "ft_water_reminder.py",
    "ft_count_harvest_iterative": ROOT_DIR / "ex5" / "ft_count_harvest_iterative.py",
    "ft_count_harvest_recursive": ROOT_DIR / "ex5" / "ft_count_harvest_recursive.py",
    "ft_garden_summary": ROOT_DIR / "ex6" / "ft_garden_summary.py",
    "ft_seed_inventory": ROOT_DIR / "ex7" / "ft_seed_inventory.py",
}


def load_module_from_file(function_name: str):
    """Load a Python module from exercise file path."""
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


def test_ft_exercise(exercise_file_name):
    """Try to run one exercise function by its exact name."""
    print(f"\n=== Testing {exercise_file_name} ===")

    try:
        ft_module = load_module_from_file(exercise_file_name)
        ft_function = getattr(ft_module, exercise_file_name)

        if exercise_file_name == "ft_seed_inventory":
            print("Testing with different seed types and units:\n")
            ft_function("tomato", 15, "packets")
            ft_function("carrot", 8, "grams")
            ft_function("lettuce", 12, "area")
            print("\nTesting with unknown unit:")
            ft_function("basil", 5, "unknown")
        else:
            ft_function()

    except ImportError as error:
        print(f"❌ Could not load exercise file: {error}")
    except AttributeError:
        print(f"❌ Could not find function {exercise_file_name}() in your file")
        print(f"   Make sure you have: def {exercise_file_name}():")
    except TypeError as error:
        msg = str(error)
        if "missing" in msg and "required positional argument" in msg:
            print(f"❌ Function signature error: {error}")
            print("   For exercise 7, use this signature:")
            print(
                f"   def {exercise_file_name}"
                "(seed_type: str, quantity: int, unit: str) -> None:"
            )
        else:
            print(f"❌ Type error: {error}")
            print("   Check your function parameters and types")
    except Exception as error:
        print(f"❌ Error running your function: {error}")
        print("   Check your code for syntax errors")


def main():
    """Run test menu for all exercises."""
    print("🌱 Welcome to Growing Code! 🌱")
    print("This helper will test your exercises for you.")
    print("\nWhich exercise would you like to test?")
    print()
    print("0 - ft_hello_garden     (Say hello to the garden community)")
    print("1 - ft_plot_area        (Calculate garden plot area)")
    print("2 - ft_harvest_total    (Add up harvest weights)")
    print("3 - ft_plant_age        (Check if plant is ready)")
    print("4 - ft_water_reminder   (Check if plants need water)")
    print("5 - ft_count_harvest    (Count days to harvest)")
    print("6 - ft_garden_summary   (Display garden info)")
    print("7 - ft_seed_inventory   (Seed inventory with type hints)")
    print("a - test all exercises")
    print()

    choice = input("Enter your choice: ")

    if choice == "0":
        test_ft_exercise("ft_hello_garden")
    elif choice == "1":
        test_ft_exercise("ft_plot_area")
    elif choice == "2":
        test_ft_exercise("ft_harvest_total")
    elif choice == "3":
        test_ft_exercise("ft_plant_age")
    elif choice == "4":
        test_ft_exercise("ft_water_reminder")
    elif choice == "5":
        test_ft_exercise("ft_count_harvest_iterative")
        test_ft_exercise("ft_count_harvest_recursive")
    elif choice == "6":
        test_ft_exercise("ft_garden_summary")
    elif choice == "7":
        test_ft_exercise("ft_seed_inventory")
    elif choice == "a":
        test_ft_exercise("ft_hello_garden")
        test_ft_exercise("ft_plot_area")
        test_ft_exercise("ft_harvest_total")
        test_ft_exercise("ft_plant_age")
        test_ft_exercise("ft_water_reminder")
        test_ft_exercise("ft_count_harvest_iterative")
        test_ft_exercise("ft_count_harvest_recursive")
        test_ft_exercise("ft_garden_summary")
        test_ft_exercise("ft_seed_inventory")
    else:
        print("❌ Invalid choice! Please enter 0, 1, 2, 3, 4, 5, 6, 7, or a")


if __name__ == "__main__":
    main()
