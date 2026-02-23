#!/usr/bin/env python3


class SecurePlant:
    """Plant with protected fields and safe setters.

    Q: Why use _height and _age?
    A: It signals internal data and encourages safe access methods.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """Create plant and validate initial values through setters."""
        self.name = name
        self._height = 0
        self._age = 0
        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        """Set height only if value is valid."""
        if (height < 0):
            print(
                "Invalid operation attempted:"
                f" height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        """Set age only if value is valid."""
        if (age < 0):
            print(
                "Invalid operation attempted:"
                f" age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self) -> int:
        """Return current safe height."""
        return self._height

    def get_age(self) -> int:
        """Return current safe age."""
        return self._age


def ft_garden_security() -> None:
    """Run a small demo of validation and protected access."""
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 25, 30)
    plant.set_height(-5)
    print(
        f"Current plant: {plant.name} "
        f"({plant.get_height()}cm, {plant.get_age()} days)")


if __name__ == "__main__":
    ft_garden_security()
