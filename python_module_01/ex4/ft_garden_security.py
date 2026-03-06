#!/usr/bin/env python3


class SecurePlant:
    """Plant with protected fields and safe setters."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Create plant and validate initial values through setters."""
        self.name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {self.name}")
        self.height = height
        self.age = age
        # Alternative approach without @property
        # self.set_height(height)
        # self.set_age(age)

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int) -> None:
        """Set height only if value is valid."""
        if (height < 0):
            print(
                "Invalid operation attempted:"
                f" height {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    # def set_height(self, height: int) -> None:
    #     """Set height only if value is valid."""
    #     if (height < 0):
    #         print(
    #             "Invalid operation attempted:"
    #             f" height {height}cm [REJECTED]")
    #         print("Security: Negative height rejected\n")
    #     else:
    #         self.__height = height
    #         print(f"Height updated: {height}cm [OK]")

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int) -> None:
        """Set age only if value is valid."""
        if (age < 0):
            print(
                "Invalid operation attempted:"
                f" age {age} days [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]\n")

    # Alternative approach without @property

    # def set_age(self, age: int) -> None:
    #     """Set age only if value is valid."""
    #     if (age < 0):
    #         print(
    #             "Invalid operation attempted:"
    #             f" age {age} days [REJECTED]")
    #         print("Security: Negative age rejected\n")
    #     else:
    #         self.__age = age
    #         print(f"Age updated: {age} days [OK]\n")

    # def get_height(self) -> int:
    #     """Return current safe height."""
    #     return self.__height

    # def get_age(self) -> int:
    #     """Return current safe age."""
    #     return self.__age


def ft_garden_security() -> None:
    """Run a small demo of validation and protected access."""
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 25, 30)
    plant.height = -5
    # plant.set_height(-5)
    print(
        f"Current plant: {plant.name} "
        f"({plant.height}cm, {plant.age} days)")
    # f"({plant.get_height()}cm, {plant.get_age()} days)")


if __name__ == "__main__":
    ft_garden_security()
