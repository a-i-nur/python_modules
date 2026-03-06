#!/usr/bin/env python3


class Plant:
    """Plant with shared counter of created objects."""

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

    def print_total_plants(self) -> None:
        """Print total number of created plants."""
        print(f"\nTotal plants created: {self._total_plants}")


def ft_plant_factory() -> None:
    """Create many plants from one source list."""
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
    new_plant.print_total_plants()


if __name__ == "__main__":
    ft_plant_factory()
