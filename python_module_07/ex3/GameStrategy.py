"""Strategy interface for engine decision-making."""

from abc import ABC, abstractmethod
from typing import Any


class GameStrategy(ABC):
    """Interface for turn execution strategies."""

    @abstractmethod
    def execute_turn(
        self,
        hand: list[Any],
        battlefield: list[Any],
    ) -> dict[str, Any]:
        """Execute one turn using the current hand and battlefield."""
        raise NotImplementedError

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Return the strategy name for engine reports."""
        raise NotImplementedError

    @abstractmethod
    def prioritize_targets(self, available_targets: list[Any]) -> list[Any]:
        """Return the targets sorted by priority."""
        raise NotImplementedError
