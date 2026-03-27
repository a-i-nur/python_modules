"""ex1/Deck.py

Менеджер колоды.
Требования сабжа (Exercise 1):
- add/remove/shuffle/draw/get_deck_stats.
"""

import random
from typing import Any

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard


class Deck:
    """Хранит набор карт и предоставляет полиморфные операции поверх Card."""

    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("В колоду можно добавлять только экземпляры Card")
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for index, card in enumerate(self.cards):
            if card.name == card_name:
                del self.cards[index]
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise IndexError("Колода пуста")
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict[str, Any]:
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
