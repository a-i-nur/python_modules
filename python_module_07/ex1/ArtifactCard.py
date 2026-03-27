"""ex1/ArtifactCard.py

Конкретная карта артефакта для постоянных эффектов.
Требования сабжа (Exercise 1):
- durability и effect;
- play + activate_ability;
- артефакт живет, пока не исчерпает прочность.
"""

from typing import Any
from ex0.Card import Card


class ArtifactCard(Card):
    """Карта-артефакт с долговременным эффектом."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        durability: int,
        effect: str,
    ) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(durability, int) or durability <= 0:
            raise ValueError(
                "durability должен быть положительным целым числом"
            )
        if not isinstance(effect, str) or not effect.strip():
            raise ValueError("effect должен быть непустой строкой")

        self.durability: int = durability
        self.effect: str = effect.strip()

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}",
            # "artifact_in_play": True,
        }

    def activate_ability(self) -> dict[str, Any]:
        # Каждая активация тратит 1 durability.
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
