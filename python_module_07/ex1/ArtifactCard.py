"""Artifact card implementation for persistent effects."""

from typing import Any
from ex0.Card import Card


class ArtifactCard(Card):
    """Artifact card with a persistent effect."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        durability: int,
        effect: str,
    ) -> None:
        """Initialize artifact durability and effect text."""
        super().__init__(name, cost, rarity)
        if not isinstance(durability, int) or durability <= 0:
            raise ValueError("durability must be a positive integer")
        if not isinstance(effect, str) or not effect.strip():
            raise ValueError("effect must be a non-empty string")

        self.durability: int = durability
        self.effect: str = effect.strip()

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """Return the artifact play result."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}",
        }

    def activate_ability(self) -> dict[str, Any]:
        """Activate the artifact and spend one durability point."""
        if self.durability <= 0:
            return {
                "artifact": self.name,
                "activated": False,
                "status": "destroyed",
            }

        self.durability -= 1
        return {
            "artifact": self.name,
            "activated": True,
            "effect": self.effect,
            "remaining_durability": self.durability,
        }
