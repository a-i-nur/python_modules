#!/usr/bin/env python3


def ft_garden_intro() -> None:
    """Show one plant with basic values.

    Q: Why use variables first?
    A: It is easier to change data in one place.
    """
    plant_name = "Rose"
    plant_height = "25cm"
    plant_age = "30 days"
    print("=== Welcome to My Garden ===")
    print(f"Plant: {plant_name}")
    print(f"Height: {plant_height}")
    print(f"Age: {plant_age}")
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
