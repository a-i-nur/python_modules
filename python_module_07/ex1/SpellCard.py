"""ex1/SpellCard.py

Конкретная карта заклинания для Deck Builder.
Требования сабжа (Exercise 1):
- унаследовать Card;
- иметь effect_type;
- реализовать play и resolve_effect.
"""

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
    """Карта-однократный эффект.

    После розыгрыша считается израсходованной.
    """

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        effect_type: str,
    ) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(effect_type, str) or not effect_type.strip():
            raise ValueError("effect_type должен быть непустой строкой")
        normalized_effect_type = effect_type.strip().lower()
        if normalized_effect_type not in [item.value for item in EffectType]:
            raise ValueError("effect_type имеет недопустимое значение")
        self.effect_type: str = normalized_effect_type

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        # Эффект делаем простым (по сабжу не требуется сложная боевая логика).
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
        # Отдельный метод из сабжа:
        # здесь можно показать, на кого применили эффект.
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
