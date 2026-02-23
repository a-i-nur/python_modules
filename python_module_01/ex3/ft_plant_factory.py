#!/usr/bin/env python3


class Plant:
    """Plant with shared counter of created objects.

    Q: Why keep a class counter?
    A: It tracks all created plants in one place.
    """

    _total_plants = 0

    def __init__(self, name: str, height: int, days: int) -> None:
        """Create one plant and increment global plant count."""
        self.name = name
        self.height = height
        self.days = days
        Plant._total_plants += 1

    def print_info(self) -> None:
        """Print one created plant."""
        print(f"Created: {self.name} ({self.height}cm, {self.days} days)")

    def print_total_plants() -> None:
        """Print total number of created plants.

        Q: Why call this from class and not instance?
        A: It uses class data, not one specific plant.
        """
        print(f"\nTotal plants created: {Plant._total_plants}")


def ft_plant_factory() -> None:
    """Create many plants from one source list.

    Q: Why keep tuples in a list first?
    A: It makes mass creation short and clean.
    """
    plants = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]
    print("=== Plant Factory Output ===")
    for plant in plants:
        new_plant = Plant(*plant)
        new_plant.print_info()
    Plant.print_total_plants()


if __name__ == "__main__":
    ft_plant_factory()
