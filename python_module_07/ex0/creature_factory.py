from abc import ABC, abstractmethod

from .creature import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):

    def create_base(self) -> Creature:
        base_flame_creature = Flameling("Flameling")
        return base_flame_creature

    def create_evolved(self) -> Creature:
        evolved_flame_creature = Pyrodon("Pyrodon")
        return evolved_flame_creature


class AquaFactory(CreatureFactory):

    def create_base(self) -> Creature:
        base_aqua_creature = Aquabub("Aquabub")
        return base_aqua_creature

    def create_evolved(self) -> Creature:
        evolved_aqua_creature = Torragon("Torragon")
        return evolved_aqua_creature
