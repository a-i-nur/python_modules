"""Abstract factory interface for themed card creation."""

from abc import ABC, abstractmethod
from typing import Any

from ex0.Card import Card


class CardFactory(ABC):
    """Interface for creating themed cards and decks."""

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Create a creature card."""
        raise NotImplementedError

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Create a spell card."""
        raise NotImplementedError

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Create an artifact card."""
        raise NotImplementedError

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict[str, Any]:
        """Create a themed deck of the requested size."""
        raise NotImplementedError

    @abstractmethod
    def get_supported_types(self) -> dict[str, list[str]]:
        """Return the supported card types."""
        raise NotImplementedError
