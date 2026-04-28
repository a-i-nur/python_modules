from ex0.creature import Creature
from .capabilities import HealCapability


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Grass")

    def attack(self) -> str:
        message = f"{self.name} uses Vine Whip!"
        return message

    def heal(self) -> str:
        message = f"{self.name} heals itself for a small amount"
        return message


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Grass/Fairy")

    def attack(self) -> str:
        message = f"{self.name} uses Petal Dance!"
        return message

    def heal(self) -> str:
        message = f"{self.name} heals itself and others for a large amount"
        return message
