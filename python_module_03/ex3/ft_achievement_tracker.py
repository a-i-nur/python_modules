#!/usr/bin/env python3


def ft_achievement_tracker() -> None:
    """Show set operations for achievements and player communities."""
    print("=== Achievement Tracker System ===")
    print()

    alice = {
        'first_kill', 'level_10',
        'treasure_hunter', 'speed_demon'}
    bob = {
        'first_kill', 'level_10',
        'boss_slayer', 'collector'}
    charlie = {
        'level_10', 'treasure_hunter', 'boss_slayer',
        'speed_demon', 'perfectionist'}

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print()

    print("=== Achievement Analytics ===")
    all_achieves = set.union(alice, bob, charlie)
    print(f"All unique achievements: {all_achieves}")
    print(f"Total unique achievements: {len(all_achieves)}")
    print()

    common_achieves = set.intersection(alice, bob, charlie)
    print(f"Common to all players: {common_achieves}")

    rare = set()
    for ach in all_achieves:
        owners = 0
        if ach in alice:
            owners += 1
        if ach in bob:
            owners += 1
        if ach in charlie:
            owners += 1
        if owners == 1:
            rare.add(ach)
    print(f"Rare achievements (1 player): {rare}")
    print()

    alice_bob_common = alice.intersection(bob)
    print(f"Alice vs Bob common: {alice_bob_common}")

    alice_unique = alice.difference(bob)
    print(f"Alice unique: {alice_unique}")

    bob_unique = bob.difference(alice)
    print(f"Bob unique: {bob_unique}")
    print()

    print("=== Missing Achievements ===")
    alice_missing = all_achieves.difference(alice)
    bob_missing = all_achieves.difference(bob)
    charlie_missing = all_achieves.difference(charlie)
    print(f"Alice missing: {alice_missing}")
    print(f"Bob missing: {bob_missing}")
    print(f"Charlie missing: {charlie_missing}")
    print()

    print("=== Player Communities ===")
    alice_bob_shared = alice.intersection(bob)
    alice_charlie_shared = alice.intersection(charlie)
    bob_charlie_shared = bob.intersection(charlie)
    print(f"Alice & Bob shared: {alice_bob_shared}")
    print(f"Alice & Charlie shared: {alice_charlie_shared}")
    print(f"Bob & Charlie shared: {bob_charlie_shared}")


if __name__ == "__main__":
    ft_achievement_tracker()
