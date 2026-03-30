"""Concrete aggressive strategy implementation."""

from typing import Any

from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Spend mana quickly to maximize pressure and damage."""

    def execute_turn(
        self,
        hand: list[Any],
        battlefield: list[Any],
    ) -> dict[str, Any]:
        """Play low-cost cards first and maximize immediate damage."""
        actions: dict[str, Any] = {
            "cards_played": [],
            "mana_used": 0,
            "targets_attacked": [],
            "damage_dealt": 0,
        }
        cards_to_play: list[Any] = []

        # Aggressive play prefers cheap cards to build pressure quickly.
        sorted_hand = sorted(hand, key=lambda card: getattr(card, "cost", 0))
        mana_pool = 6

        for card in sorted_hand:
            card_cost = getattr(card, "cost", 0)
            if actions["mana_used"] + card_cost > mana_pool:
                continue

            actions["cards_played"].append(getattr(card, "name", "Unknown"))
            actions["mana_used"] += card_cost
            cards_to_play.append(card)

            damage = getattr(card, "attack", getattr(card, "attack_power", 0))
            if damage == 0 and getattr(card, "effect_type", "") == "damage":
                # Treat offensive spells as fixed turn damage in this demo.
                damage = 6
            actions["damage_dealt"] += damage

        for card in cards_to_play:
            hand.remove(card)
        battlefield.extend(cards_to_play)

        targets = self.prioritize_targets(["Enemy Player", "Enemy Creature"])
        if targets:
            actions["targets_attacked"].append(str(targets[0]))

        return actions

    def get_strategy_name(self) -> str:
        """Return the strategy name."""
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list[Any]) -> list[Any]:
        """Prioritize the enemy player before all other targets."""
        return sorted(
            available_targets,
            key=lambda t: 0 if "Player" in str(t) else 1,
        )
