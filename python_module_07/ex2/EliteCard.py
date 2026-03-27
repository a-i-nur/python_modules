"""Elite card implementation using multiple inheritance."""

from enum import Enum
from typing import Any

from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """Elite card with both combat and magic abilities."""

    class SpellName(Enum):
        """Known spell names for elite cards."""

        FIREBALL = "Fireball"
        ICE_LANCE = "Ice Lance"
        ARCANE_BURST = "Arcane Burst"

    _SPELL_COST: dict[str, int] = {
        SpellName.FIREBALL.value: 4,
        SpellName.ICE_LANCE.value: 2,
        SpellName.ARCANE_BURST.value: 3,
    }

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        health: int,
        mana: int,
    ) -> None:
        """Initialize an elite card with combat and mana stats."""
        super().__init__(name, cost, rarity)

        if not isinstance(attack_power, int) or attack_power <= 0:
            raise ValueError("attack_power must be a positive integer")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("health must be a positive integer")
        if not isinstance(mana, int) or mana < 0:
            raise ValueError("mana must be an integer >= 0")

        self.attack_power: int = attack_power
        self.health: int = health
        self.mana: int = mana

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """Return the play result for the elite card."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "status": "Elite card enters battlefield",
        }

    def attack(self, target: Any) -> dict[str, Any]:
        """Deal melee damage to a target."""
        try:
            target_name = target.name
        except Exception:
            target_name = str(target)
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        """Block part of the incoming damage and update health."""
        if incoming_damage < 0:
            raise ValueError("incoming_damage cannot be negative")

        # Block up to 40% of the incoming damage.
        blocked = int(incoming_damage * 0.4)
        taken = incoming_damage - blocked
        self.health = max(0, self.health - taken)

        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict[str, Any]:
        """Return the current combat attributes."""
        return {"attack_power": self.attack_power, "health": self.health}

    def cast_spell(
        self,
        spell_name: str,
        targets: list[Any],
    ) -> dict[str, Any]:
        """Cast a spell if enough mana is available."""
        canonical_spell = spell_name.strip()
        mana_used = self._SPELL_COST.get(canonical_spell, 2)
        if self.mana < mana_used:
            return {
                "caster": self.name,
                "spell": canonical_spell,
                "status": "Not enough mana",
                "mana_used": 0,
            }

        self.mana -= mana_used
        target_names: list[str] = []
        for target in targets:
            try:
                target_names.append(target.name)
            except Exception:
                target_names.append(str(target))
        return {
            "caster": self.name,
            "spell": canonical_spell,
            "targets": target_names,
            "mana_used": mana_used,
        }

    def channel_mana(self, amount: int) -> dict[str, Any]:
        """Add mana to the card."""
        if amount < 0:
            raise ValueError("amount cannot be negative")
        self.mana += amount
        return {"channeled": amount, "total_mana": self.mana}

    def get_magic_stats(self) -> dict[str, Any]:
        """Return the current mana pool and known spells."""
        return {
            "mana": self.mana,
            "known_spells": [
                spell.value for spell in self.SpellName
            ],
        }
