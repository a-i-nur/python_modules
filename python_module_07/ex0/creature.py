from abc import ABC, abstractmethod


class Creature(ABC):

    def __init__(self, name: str, creature_type: str) -> None:
        self.name = name
        self.creature_type = creature_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        message = f"{self.name} is a {self.creature_type} type Creature"
        return message


class Flameling(Creature):

    def __init__(self, name: str) -> None:
        super().__init__(name, "Fire")

    def attack(self) -> str:
        message = f"{self.name} uses Ember!"
        return message


class Pyrodon(Creature):

    def __init__(self, name: str) -> None:
        super().__init__(name, "Fire/Flying")

    def attack(self) -> str:
        message = f"{self.name} uses Flamethrower!"
        return message


class Aquabub(Creature):

    def __init__(self, name: str) -> None:
        super().__init__(name, "Water")

    def attack(self) -> str:
        message = f"{self.name} uses Water Gun!"
        return message


class Torragon(Creature):

    def __init__(self, name: str) -> None:
        super().__init__(name, "Water")

    def attack(self) -> str:
        message = f"{self.name} uses Hydro Pump!"
        return message
