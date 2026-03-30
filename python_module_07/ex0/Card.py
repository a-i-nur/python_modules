"""Base card contract for the DataDeck project."""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Any


class Rarity(Enum):
    """Allowed rarity values."""

    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


class Card(ABC):
    """Abstract base class for all cards."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """Initialize the shared card fields."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")
        if not isinstance(cost, int) or cost < 0:
            raise ValueError("cost must be an integer >= 0")
        if not isinstance(rarity, str) or not rarity.strip():
            raise ValueError("rarity must be a non-empty string")
        normalized_rarity = rarity.strip()
        if normalized_rarity not in [item.value for item in Rarity]:
            raise ValueError("rarity has an invalid value")

        self.name: str = name.strip()
        self.cost: int = cost
        self.rarity: str = normalized_rarity

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """Play the card and return a structured result."""
        raise NotImplementedError

    play = abstractmethod(play)

    def get_card_info(self) -> dict[str, Any]:
        """Return shared card metadata."""
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.__class__.__name__.replace("Card", ""),
        }

    def is_playable(self, available_mana: int) -> bool:
        """Return whether the current mana pool can pay the card cost."""
        if available_mana < self.cost:
            return False
        return True
