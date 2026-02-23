#!/usr/bin/env python3


class Plant:
    """Base plant used in the garden network."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Set common plant values."""
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        """Increase plant height by one centimeter."""
        self.height += 1
        print(f"{self.name} grew 1cm")

    def print_info(self) -> None:
        """Print base plant info."""
        print(f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    """Plant that can bloom and has a flower color."""

    def __init__(
            self, name: str, height: int, age: int,
            color: str, blooming: bool = True) -> None:
        """Set base values and flowering values."""
        super().__init__(name, height, age)
        self.color = color
        self.blooming = blooming

    def print_info(self) -> None:
        """Print flowering plant info with bloom status."""
        if self.blooming:
            blooming_status = "blooming"
        else:
            blooming_status = "not blooming"
        print(
            f"- {self.name}: {self.height}cm, "
            f"{self.color} flowers ({blooming_status})")


class PrizeFlower(FloweringPlant):
    """Flowering plant with extra prize points."""

    def __init__(
            self, name: str, height: int, age: int,
            color: str, score: int, blooming: bool = True) -> None:
        """Set flowering fields and prize score."""
        super().__init__(name, height, age, color, blooming)
        self.score = score

    def print_info(self) -> None:
        """Print prize flower info."""
        if self.blooming:
            blooming_status = "blooming"
        else:
            blooming_status = "not blooming"
        print(
            f"- {self.name}: {self.height}cm, "
            f"{self.color} flowers ({blooming_status}), "
            f"Prize points: {self.score}")


class GardenManager:
    """Manager that stores many gardens and reports analytics.

    Q: Why put stats helper inside manager?
    A: Stats logic belongs to manager domain and stays grouped here.
    """

    def __init__(self) -> None:
        """Create empty garden storage."""
        self.gardens: dict = {}

    @classmethod
    def create_garden_network(cls) -> "GardenManager":
        """Build a manager from class level.

        Q: Why classmethod here?
        A: It creates an instance from the class itself.
        """
        return cls()

    @staticmethod
    def is_valid_height(height: int) -> bool:
        """Check if height is a non-negative integer.

        Q: Why staticmethod?
        A: This check needs no object or class state.
        """
        return isinstance(height, int) and height >= 0

    def add_garden(self, owner: str) -> None:
        """Add a garden record for one owner."""
        self.gardens[owner] = {
            "plants": [],
            "stats": {"plants_added": 0, "total_growth": 0}
        }

    def add_plant(self, owner: str, plant: Plant) -> None:
        """Add one plant and update counters."""
        self.gardens[owner]["plants"].append(plant)
        self.gardens[owner]["stats"]["plants_added"] += 1
        print(f"Added {plant.name} to {owner}'s garden")

    def help_plants_grow(self, owner: str) -> None:
        """Grow all plants in one owner garden by one step."""
        print(f"{owner} is helping all plants grow...")

        for plant in self.gardens[owner]["plants"]:
            plant.grow()
            self.gardens[owner]["stats"]["total_growth"] += 1

    def report(self, owner: str) -> None:
        """Print full report for one owner."""
        garden_data = self.gardens[owner]

        print(f"\n=== {owner}'s Garden Report ===")
        print("Plants in garden:")

        for plant in garden_data["plants"]:
            plant.print_info()
        print("")

        added = self.GardenStats.plants_added(garden_data)
        growth = self.GardenStats.total_growth(garden_data)
        print(f"Plants added: {added}, Total growth: {growth}cm")

        regular, flowering, prize = self.GardenStats.type_breakdown(
            garden_data)
        print(
            f"Plant types: {regular} regular, {flowering} flowering, "
            f"{prize} prize flowers")

    def compare_garden_scores(self) -> None:
        """Print score summary for each garden."""
        parts = []
        for owner, garden_data in self.gardens.items():
            score = self.GardenStats.garden_score(garden_data)
            parts.append(f"{owner}: {score}")
        print("Garden scores - " + ", ".join(parts))

    def total_gardens(self) -> int:
        """Return number of managed gardens."""
        return len(self.gardens)

    class GardenStats:
        """Nested helper for analytics calculations."""

        @staticmethod
        def plants_added(garden_data: dict) -> int:
            """Return how many plants were added."""
            return garden_data["stats"]["plants_added"]

        @staticmethod
        def total_growth(garden_data: dict) -> int:
            """Return total growth in centimeters."""
            return garden_data["stats"]["total_growth"]

        @staticmethod
        def type_breakdown(garden_data: dict) -> tuple[int, int, int]:
            """Count regular, flowering, and prize plants."""
            regular = 0
            flowering = 0
            prize = 0

            for plant in garden_data["plants"]:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1

            return regular, flowering, prize

        @staticmethod
        def garden_score(garden_data: dict) -> int:
            """Calculate total garden score from all components.

            Q: Why combine height, bloom bonus, and prize score?
            A: It gives one simple number for quick comparison.
            """
            total = 0
            blooming_bonus = 0
            prize_points = 0

            for plant in garden_data["plants"]:
                total += plant.height
                if isinstance(plant, PrizeFlower):
                    prize_points += plant.score
                if isinstance(plant, FloweringPlant) and plant.blooming:
                    blooming_bonus += 15

            return total + prize_points + blooming_bonus


def ft_garden_analytics() -> None:
    """Run a complete demo of manager, plants, and analytics."""
    print("=== Garden Management System Demo ===\n")
    garden_manager = GardenManager.create_garden_network()

    garden_manager.add_garden("Alice")
    garden_manager.add_garden("Bob")

    oak = Plant("Oak Tree", 100, 10)
    rose = FloweringPlant("Rose", 25, 5, "red", True)
    sun_flower = PrizeFlower("Sunflower", 50, 3, "yellow", 10, True)

    garden_manager.add_plant("Alice", oak)
    garden_manager.add_plant("Alice", rose)
    garden_manager.add_plant("Alice", sun_flower)
    garden_manager.add_plant("Bob", Plant("Cactus", 92, 20))
    print("")

    garden_manager.help_plants_grow("Alice")
    garden_manager.report("Alice")
    print("")

    print("Height validation test:", GardenManager.is_valid_height(oak.height))
    garden_manager.compare_garden_scores()
    print("Total gardens managed:", garden_manager.total_gardens())


if __name__ == "__main__":
    ft_garden_analytics()
