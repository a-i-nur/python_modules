from ex0 import CreatureFactory
from .healing_creatures import Sproutling, Bloomelle
from .transform_creatures import Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> Sproutling:
        base_healing_creature = Sproutling("Sproutling")
        return base_healing_creature

    def create_evolved(self) -> Bloomelle:
        evolved_healing_creature = Bloomelle("Bloomelle")
        return evolved_healing_creature


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        base_transform_creature = Shiftling("Shiftling")
        return base_transform_creature

    def create_evolved(self) -> Morphagon:
        evolved_transform_creature = Morphagon("Morphagon")
        return evolved_transform_creature
