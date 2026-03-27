"""Spell card implementation for the deck builder layer."""

from enum import Enum
from typing import Any

from ex0.Card import Card


class EffectType(Enum):
    """Allowed spell effect types."""

    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    """One-shot spell card."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        effect_type: str,
    ) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(effect_type, str) or not effect_type.strip():
            raise ValueError("effect_type must be a non-empty string")
        normalized_effect_type = effect_type.strip().lower()
        if normalized_effect_type not in [item.value for item in EffectType]:
            raise ValueError("effect_type has an invalid value")
        self.effect_type: str = normalized_effect_type

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """Return a simple play result for the spell."""
        effect_map = {
            "damage": "Deal 3 damage to target",
            "heal": "Restore 3 health to ally",
            "buff": "+2 attack to ally this turn",
            "debuff": "-2 attack to enemy this turn",
        }
        effect_text = effect_map.get(
            self.effect_type,
            f"Apply {self.effect_type} effect",
        )
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect_text,
            # "consumed": True,
        }

    def resolve_effect(self, targets: list[Any]) -> dict[str, Any]:
        """Resolve the spell effect against the given targets."""
        target_names: list[str] = []
        for target in targets:
            try:
                target_names.append(target.name)
            except Exception:
                target_names.append(str(target))
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": target_names,
            "resolved": True,
        }
