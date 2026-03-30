"""Concrete factory for fantasy-themed cards."""

import random
from typing import Any

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    """Factory for dragons, spells, and magical artifacts."""

    def __init__(self) -> None:
        """Initialize the predefined fantasy card pools."""
        self._creatures: list[tuple[str, int, str, int, int]] = [
            ("Fire Dragon", 5, "Legendary", 7, 5),
            ("Goblin Warrior", 2, "Common", 2, 1),
            ("Ice Wizard", 4, "Rare", 3, 4),
        ]
        self._spells: list[tuple[str, int, str, str]] = [
            ("Fireball", 4, "Rare", "damage"),
            ("Lightning Bolt", 3, "Common", "damage"),
            ("Healing Wave", 3, "Common", "heal"),
            ("War Cry", 2, "Common", "buff"),
        ]
        self._artifacts: list[tuple[str, int, str, int, str]] = [
            ("Mana Ring", 2, "Rare", 3, "+1 mana per turn"),
            ("Staff of Embers", 3, "Epic", 2, "+2 spell damage"),
        ]

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Create a creature card, optionally overriding name or attack."""
        name, cost, rarity, attack, health = random.choice(self._creatures)
        if isinstance(name_or_power, str) and name_or_power.strip():
            name = name_or_power.strip()
        if isinstance(name_or_power, int) and name_or_power > 0:
            attack = name_or_power
        return CreatureCard(name, cost, rarity, attack, health)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Create a spell card, optionally overriding its name."""
        name, cost, rarity, effect_type = random.choice(self._spells)
        if isinstance(name_or_power, str) and name_or_power.strip():
            name = name_or_power.strip()
        return SpellCard(name, cost, rarity, effect_type)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Create an artifact card with optional overrides."""
        name, cost, rarity, durability, effect = random.choice(self._artifacts)
        if isinstance(name_or_power, int) and name_or_power > 0:
            durability = name_or_power
        if isinstance(name_or_power, str) and name_or_power.strip():
            name = name_or_power.strip()
        return ArtifactCard(name, cost, rarity, durability, effect)

    def create_themed_deck(self, size: int) -> dict[str, Any]:
        if size <= 0:
            raise ValueError("size must be > 0")

        # Keep the initial sample deterministic so main.py stays stable.
        base_cards: list[Card] = [
            CreatureCard("Fire Dragon", 5, "Legendary", 7, 5),
            CreatureCard("Goblin Warrior", 2, "Common", 2, 1),
            SpellCard("Lightning Bolt", 3, "Common", "damage"),
        ]
        cards: list[Card] = []
        for index in range(size):
            if index < len(base_cards):
                cards.append(base_cards[index])
            else:
                cards.append(random.choice(base_cards))

        return {
            "theme": "Fantasy",
            "size": size,
            "cards": cards,
        }

    def get_supported_types(self) -> dict[str, list[str]]:
        """Return the fantasy card families supported by the factory."""
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"],
        }
