from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple:
        return spell1(target, power), spell2(target, power)

    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"

    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence_spell(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return sequence_spell


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} with {power} power"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def has_enough_power(target: str, power: int) -> bool:
    return power >= 10


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(f"Combined spell result: {combined('Dragon', 10)}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: 10, Amplified: {mega_fireball('Dragon', 10)}")

    print("\nTesting conditional caster...")
    safe_fireball = conditional_caster(has_enough_power, fireball)
    print(safe_fireball("Dragon", 15))
    print(safe_fireball("Dragon", 5))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal])
    print(sequence("Dragon", 10))


if __name__ == "__main__":
    main()
