#!/usr/bin/env python3

class GardenError(Exception):
    """A basic error for garden problems."""
    pass


class PlantError(GardenError):
    """For problems with plants (inherits from GardenError)"""
    pass


class WaterError(GardenError):
    """For problems with watering (inherits from GardenError)"""
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants: dict[str, dict[str, int]] = {}
        self.water_tank: int = 10

    def add_plant(
            self,
            name: str,
            water: int | None = None,
            sun: int | None = None) -> None:
        if not name:
            raise PlantError("Plant name cannot be empty!")
        if water is None:
            water = 5
        if sun is None:
            sun = 8
        self.plants[name] = {"water": water, "sun": sun}
        print(f"Added {name} successfully")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                if self.water_tank <= 0:
                    raise WaterError("Not enough water in tank")
                print(f"Watering {plant} - success")
                self.water_tank -= 1
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(
        self,
        plant_name: str,
    ) -> str:
        if not plant_name:
            raise ValueError("Plant name cannot be empty!")
        if plant_name not in self.plants:
            raise PlantError(
                f"Plant '{plant_name}' not found!")
        if self.plants[plant_name]["water"] < 1:
            raise ValueError(
                f"Water level {self.plants[plant_name]["water"]} "
                "is too low (min 1)")
        if self.plants[plant_name]["water"] > 10:
            raise ValueError(
                f"Water level {self.plants[plant_name]["water"]} "
                "is too high (max 10)")
        if self.plants[plant_name]["sun"] < 2:
            raise ValueError(
                f"Sunlight hours {self.plants[plant_name]["sun"]} "
                "is too low (min 2)")
        if self.plants[plant_name]["sun"] > 12:
            raise ValueError(
                f"Sunlight hours {self.plants[plant_name]["sun"]} "
                "is too high (max 12)")
        return (
            f"{plant_name}: healthy "
            f"(water: {self.plants[plant_name]["water"]}, "
            f"sun: {self.plants[plant_name]["sun"]})")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    manager = GardenManager()

    print("Adding plants to garden...")
    try:
        manager.add_plant("tomato", 5, 8)
        manager.add_plant("lettuce", 15, 6)
        manager.add_plant("")
    except PlantError as e:
        print(f"Error adding plant: {e}")
    print()

    print("Watering plants...")
    try:
        manager.water_plants()
    except GardenError as e:
        print(f"Error watering plants: {e}")
    print()

    print("Checking plant health...")
    try:
        print(manager.check_plant_health("tomato"))
    except (GardenError, ValueError) as e:
        print(f"Error checking tomato: {e}")

    try:
        print(manager.check_plant_health("lettuce"))
    except (GardenError, ValueError) as e:
        print(f"Error checking lettuce: {e}")
    print()

    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")
    print()

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
