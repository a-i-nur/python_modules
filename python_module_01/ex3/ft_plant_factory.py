#!/usr/bin/env python3

class Plant:

    _total_plants = 0

    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days
        _total_plants += 1

    def print_info(self) -> None:
        print(f"Created: {self.name} ({self.height}cm, {self.days} days)")

    def ptint_total_plants() -> None:
        print(f"Total plants created: {Plant._total_plants}")


def ft_plant_factory() -> None:
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


if __name__ == "__main__":
    ft_plant_factory()
