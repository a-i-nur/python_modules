#!/usr/bin/env python3


class Plant:
    """Store common data for one plant.

    Q: Why use a class for simple data?
    A: Many plants can share the same structure.
    """

    def __init__(self, name: str, height: int, days: int) -> None:
        """Build a plant with start values."""
        self.name = name
        self.height = height
        self.days = days

    def print_info(self) -> None:
        """Print plant data in one simple line."""
        print(f"{self.name}: {self.height}cm, {self.days} days old")


def ft_garden_data() -> None:
    """Create and print a small plant registry.

    Q: Why three objects instead of three dicts?
    A: This trains object-oriented basics for next exercises.
    """
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    rose.print_info()
    sunflower.print_info()
    cactus.print_info()


if __name__ == "__main__":
    ft_garden_data()
