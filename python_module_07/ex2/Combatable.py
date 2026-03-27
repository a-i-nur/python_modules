"""Combat interface for battle-related behavior."""

from abc import ABC, abstractmethod
from typing import Any


class Combatable(ABC):
    """Interface for objects that can fight."""

    @abstractmethod
    def attack(self, target: Any) -> dict[str, Any]:
        """Attack a target and return the result."""
        raise NotImplementedError

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict[str, Any]:
        """Take incoming damage and return the defense result."""
        raise NotImplementedError

    @abstractmethod
    def get_combat_stats(self) -> dict[str, Any]:
        """Return the current combat stats."""
        raise NotImplementedError
