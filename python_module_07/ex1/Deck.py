"""Deck container and basic deck operations."""

import random
from typing import Any

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard


class Deck:
    """Store cards and expose deck-level operations."""

    def __init__(self) -> None:
        """Initialize an empty deck."""
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        """Add a card to the deck."""
        if not isinstance(card, Card):
            raise TypeError("only Card instances can be added to the deck")
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Remove the first card with the given name."""
        for index, card in enumerate(self.cards):
            if card.name == card_name:
                del self.cards[index]
                return True
        return False

    def shuffle(self) -> None:
        """Shuffle the deck in place."""
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """Draw and remove the top card from the deck."""
        if not self.cards:
            raise IndexError("deck is empty")
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict[str, Any]:
        """Return basic statistics about the deck."""
        total_cards = len(self.cards)
        if total_cards == 0:
            return {
                "total_cards": 0,
                "creatures": 0,
                "spells": 0,
                "artifacts": 0,
                "avg_cost": 0.0,
            }

        total_cost = sum(card.cost for card in self.cards)
        return {
            "total_cards": total_cards,
            "creatures": sum(
                isinstance(card, CreatureCard) for card in self.cards
            ),
            "spells": sum(isinstance(card, SpellCard) for card in self.cards),
            "artifacts": sum(
                isinstance(card, ArtifactCard) for card in self.cards
            ),
            "avg_cost": int((total_cost / total_cards) * 100) / 100,
        }
