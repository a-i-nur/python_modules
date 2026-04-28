from ex0.creature import Creature
from .capabilities import TransformCapability


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str) -> None:
        Creature.__init__(self, name, "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.transformed:
            message = f"{self.name} performs a boosted strike!"
        else:
            message = f"{self.name} attacks normally."
        return message

    def transform(self) -> str:
        self.transformed = True
        message = f"{self.name} shifts into a sharper form!"
        return message

    def revert(self) -> str:
        self.transformed = False
        message = f"{self.name} returns to normal."
        return message


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str) -> None:
        Creature.__init__(self, name, "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.transformed:
            message = f"{self.name} unleashes a devastating morph strike!"
        else:
            message = f"{self.name} attacks normally."
        return message

    def transform(self) -> str:
        self.transformed = True
        message = f"{self.name} morphs into a dragonic battle form!"
        return message

    def revert(self) -> str:
        self.transformed = False
        message = f"{self.name} stabilizes its form."
        return message
