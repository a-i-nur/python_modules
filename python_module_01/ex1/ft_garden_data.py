#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, days: int)-> None:
        self.name = name
        self.height = height
        self.days = days

    def print_info(self)-> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old")


def ft_garden_data()-> None:
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    rose.print_info()
    sunflower.print_info()
    cactus.print_info()


if __name__ == "__main__":
    ft_garden_data()
