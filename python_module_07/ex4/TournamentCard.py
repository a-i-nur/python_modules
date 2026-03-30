"""Tournament card combining combat and ranking behavior."""

from typing import Any

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """Card that can fight and participate in tournament rankings."""

    def __init__(
        self,
        card_id: str,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        health: int,
        base_rating: int = 1200,
    ) -> None:
        """Initialize a tournament card with combat and ranking stats."""
        super().__init__(name, cost, rarity)

        if not isinstance(card_id, str) or not card_id.strip():
            raise ValueError("card_id must be a non-empty string")
        if attack_power <= 0 or health <= 0:
            raise ValueError("attack_power and health must be > 0")

        self.card_id: str = card_id.strip()
        self.attack_power: int = attack_power
        self.health: int = health
        self.base_rating: int = base_rating

        self.wins: int = 0
        self.losses: int = 0

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """Return the play result for the tournament card."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament card enters arena",
        }

    def attack(self, target: Any) -> dict[str, Any]:
        """Attack a target and return the damage dealt."""
        target_name = getattr(target, "name", str(target))
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
        }

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        """Apply incoming damage and return the defense result."""
        self.health = max(0, self.health - max(0, incoming_damage))
        return {
            "defender": self.name,
            "remaining_health": self.health,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict[str, Any]:
        """Return the current combat stats."""
        return {"attack_power": self.attack_power, "health": self.health}

    def calculate_rating(self) -> int:
        """Calculate the current rating using a simple Elo-like model."""
        return self.base_rating + (self.wins * 16) - (self.losses * 16)

    def update_wins(self, wins: int) -> None:
        if wins < 0:
            raise ValueError("wins cannot be negative")
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        if losses < 0:
            raise ValueError("losses cannot be negative")
        self.losses += losses

    def get_rank_info(self) -> dict[str, Any]:
        """Return the current rating and win-loss record."""
        return {
            "rating": self.calculate_rating(),
            "record": f"{self.wins}-{self.losses}",
            "wins": self.wins,
            "losses": self.losses,
        }

    def get_tournament_stats(self) -> dict[str, Any]:
        """Return a combined tournament summary for the card."""
        return {
            "id": self.card_id,
            "name": self.name,
            "interfaces": ["Card", "Combatable", "Rankable"],
            **self.get_rank_info(),
        }
