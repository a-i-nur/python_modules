"""Game engine that connects the factory and the strategy."""

from typing import Any

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """Coordinate turn simulation and basic engine state."""

    def __init__(self) -> None:
        """Initialize an empty engine state."""
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.hand: list[Any] = []
        self.battlefield: list[Any] = []
        self.turns_simulated: int = 0
        self.total_damage: int = 0

    def configure_engine(
        self,
        factory: CardFactory,
        strategy: GameStrategy,
    ) -> None:
        """Attach a factory and strategy and reset engine state."""
        self.factory = factory
        self.strategy = strategy
        self.hand = []
        self.battlefield = []
        self.turns_simulated = 0
        self.total_damage = 0

    def simulate_turn(self) -> dict[str, Any]:
        """Simulate one turn and return a turn report."""
        if self.factory is None or self.strategy is None:
            raise RuntimeError("Engine is not configured")

        if not self.hand:
            self.hand = self.factory.create_themed_deck(3)["cards"]

        cards_created = len(self.hand)
        self.turns_simulated += 1
        turn_actions = self.strategy.execute_turn(self.hand, self.battlefield)
        self.total_damage += int(turn_actions.get("damage_dealt", 0))

        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": cards_created,
            "actions": turn_actions,
        }

    def get_engine_status(self) -> dict[str, Any]:
        """Return a snapshot of the current engine state."""
        strategy_name = (
            self.strategy.get_strategy_name()
            if self.strategy is not None
            else None
        )
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": strategy_name,
            "hand": [getattr(card, "name", "Unknown") for card in self.hand],
            "battlefield": [
                getattr(card, "name", "Unknown") for card in self.battlefield
            ],
            "total_damage": self.total_damage,
        }
