#!/usr/bin/env python3


class Plant:
    """Base class with data common to all plant kinds."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Set shared base values."""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Plant type that adds color and bloom behavior."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Build flower and call parent setup with super()."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Show flower-specific action."""
        print(f"{self.name} is blooming beautifully!\n")

    def print_info(self) -> None:
        """Print flower data and run its action."""
        print(
            f"{self.name} (Flower): {self.height}cm, {self.age} "
            f"days, {self.color} color")
        self.bloom()


class Tree(Plant):
    """Plant type that adds trunk data and shade behavior."""

    def __init__(
            self, name: str, height: int, age: int,
            trunk_diameter: int) -> None:
        """Build tree and keep trunk diameter."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Estimate and print shade area from simple geometry.

        Q: Why an approximate formula?
        A: We only need a quick demo value, not real botany precision.
        """
        aprx_crown_dmtr = (self.trunk_diameter / 100) * (self.height / 100) * 4
        aprx_shade_square = 3.14 * ((aprx_crown_dmtr / 2) ** 2)
        print(
            f"{self.name} provides {aprx_shade_square:.0f} "
            f"square meters of shade\n")

    def print_info(self) -> None:
        """Print tree data and run its action."""
        print(
            f"{self.name} (Tree): {self.height}cm, {self.age} days, "
            f"{self.trunk_diameter}cm diameter")
        self.produce_shade()


class Vegetable(Plant):
    """Plant type with harvest and nutrition data."""

    def __init__(
            self, name: str, height: int, age: int,
            harvest_season: str, nutritional_value: str) -> None:
        """Build vegetable with specific fields."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def describe_nutrition(self) -> None:
        """Show a simple nutrition message."""
        print(f"{self.name} is rich in {self.nutritional_value}\n")

    def print_info(self) -> None:
        """Print vegetable data and run its action."""
        print(
            f"{self.name} (Vegetable): {self.height}cm, "
            f"{self.age} days, {self.harvest_season} harvest")
        self.describe_nutrition()


def ft_plant_types() -> None:
    """Create two objects of each plant family type.

    Q: Why one list for all objects?
    A: One loop can call shared method names on all plant types.
    """
    print("=== Garden Plant Types ===\n")

    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")

    mandrake = Flower("Mandrake", 50, 365, "cream")
    whomping_willow = Tree("Whomping Willow", 1000, 36500, 60)
    gillyweed = Vegetable("Gillyweed", 20, 30, "autumn", "vitamin A")

    garden = [rose, oak, tomato, mandrake, whomping_willow, gillyweed]

    for plant in garden:
        plant.print_info()


if __name__ == "__main__":
    ft_plant_types()
