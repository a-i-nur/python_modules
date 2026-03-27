"""Magic interface for spell and mana behavior."""

from abc import ABC, abstractmethod
from typing import Any


class Magical(ABC):
    """Interface for objects that use mana and spells."""

    @abstractmethod
    def cast_spell(
        self,
        spell_name: str,
        targets: list[Any],
    ) -> dict[str, Any]:
        """Cast a spell on the given targets."""
        raise NotImplementedError

    @abstractmethod
    def channel_mana(self, amount: int) -> dict[str, Any]:
        """Gain mana and return the updated mana state."""
        raise NotImplementedError

    @abstractmethod
    def get_magic_stats(self) -> dict[str, Any]:
        """Return the current magic stats."""
        raise NotImplementedError
