"""ex0/CreatureCard.py

First concrete `Card` implementation for Exercise 0.
"""

from typing import Any
from .Card import Card


class CreatureCard(Card):
    """Concrete creature card."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
    ) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("attack must be a positive integer")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("health must be a positive integer")

        self.attack: int = attack
        self.health: int = health

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """Play the creature and return the summon result."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def attack_target(self, target: str | Card) -> dict[str, Any]:
        """Attack a target identified by name or by another card instance."""
        if isinstance(target, Card):
            target_name = target.name
        else:
            target_name = target
        return {
            "attacker": self.name,
            "target": target_name,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }

    def get_card_info(self) -> dict[str, Any]:
        """Return base card info extended with creature-specific stats."""
        info = super().get_card_info()
        info.update({"attack": self.attack, "health": self.health})
        return info
