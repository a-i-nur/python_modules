#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.days += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old")


def ft_plant_growth() -> None:
    plant = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    plant.get_info()
    for _ in range(6):
        plant.grow()
        plant.age()
    print("=== Day 7 ===")
    plant.get_info()


if __name__ == "__main__":
    ft_plant_growth()
