"""Tournament platform for registration, matches, and reports."""

import random
from typing import Any

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """Register tournament cards and manage matches."""

    def __init__(self) -> None:
        """Initialize an empty tournament platform."""
        self._cards: dict[str, TournamentCard] = {}
        self._matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        """Register a tournament card and return its id."""
        if card.card_id in self._cards:
            raise ValueError(
                f"Card with id '{card.card_id}' already registered"
            )
        self._cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict[str, Any]:
        """Simulate a match between two registered cards."""
        if card1_id == card2_id:
            raise ValueError("cannot create a match against the same card")

        card1 = self._cards.get(card1_id)
        card2 = self._cards.get(card2_id)
        if card1 is None or card2 is None:
            raise ValueError("both cards must be registered")

        # Match score = attack power plus a small random bonus.
        score1 = card1.attack_power + random.randint(0, 3)
        score2 = card2.attack_power + random.randint(0, 3)

        if score1 >= score2:
            winner, loser = card1, card2
        else:
            winner, loser = card2, card1

        winner.update_wins(1)
        loser.update_losses(1)
        self._matches_played += 1

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }

    def get_leaderboard(self) -> list[TournamentCard]:
        """Return the registered cards sorted by rating."""
        return sorted(
            self._cards.values(),
            key=lambda card: card.calculate_rating(),
            reverse=True,
        )

    def generate_tournament_report(self) -> dict[str, Any]:
        """Return a summary of the current tournament platform state."""
        total_cards = len(self._cards)
        avg_rating = 0
        if total_cards > 0:
            avg_rating = (
                sum(card.calculate_rating() for card in self._cards.values())
                // total_cards
            )

        return {
            "total_cards": total_cards,
            "matches_played": self._matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active" if total_cards > 0 else "idle",
        }
