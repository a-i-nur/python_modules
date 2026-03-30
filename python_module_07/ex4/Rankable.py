"""Ranking interface for tournament entities."""

from abc import ABC, abstractmethod
from typing import Any


class Rankable(ABC):
    """Interface for objects that participate in rankings."""

    def calculate_rating(self) -> int:
        """Recalculate the current rating."""
        raise NotImplementedError

    def update_wins(self, wins: int) -> None:
        """Update the number of wins."""
        raise NotImplementedError

    def update_losses(self, losses: int) -> None:
        """Update the number of losses."""
        raise NotImplementedError

    def get_rank_info(self) -> dict[str, Any]:
        """Return the current ranking summary."""
        raise NotImplementedError

    calculate_rating = abstractmethod(calculate_rating)
    update_wins = abstractmethod(update_wins)
    update_losses = abstractmethod(update_losses)
    get_rank_info = abstractmethod(get_rank_info)
