#!/usr/bin/env python3


class Plant:
    """Plant model with actions over time."""

    def __init__(self, name: str, height: int, days: int) -> None:
        """Set start state."""
        self.name = name
        self.height = height
        self.days = days
        self.growth = 0

    def grow(self) -> None:
        """Increase height by one centimeter."""
        self.height += 1
        self.growth += 1

    def age(self) -> None:
        """Increase age by one day."""
        self.days += 1

    def get_info(self) -> None:
        """Print current state."""
        print(f"{self.name}: {self.height}cm, {self.days} days old")


def ft_plant_growth() -> None:
    """Simulate one week for multiple plants."""
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    plants = [rose, sunflower, cactus]
    print("=== Day 1 ===")
    for plant in plants:
        plant.get_info()
    for _ in range(6):
        for plant in plants:
            plant.grow()
            plant.age()
    print("=== Day 7 ===")
    for plant in plants:
        plant.get_info()
        print(f"Growth this week: +{plant.growth}cm")
    for plant in plants:
        plant.growth = 0


if __name__ == "__main__":
    ft_plant_growth()
