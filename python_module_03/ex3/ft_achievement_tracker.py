#!/usr/bin/env python3
"""
Exercise 3: Achievement Tracker.

Collection theory: sets store unique, unordered elements and support
fast membership checks and algebraic operations (union, intersection,
difference). They are ideal for de-duplicating achievements and finding
overlap between players.
"""


def ft_achievement_tracker() -> None:
    """Show set operations for achievements and player communities."""
    print("=== Achievement Tracker System ===")
    print()

    alice_achieves = {
        'first_kill', 'level_10',
        'treasure_hunter', 'speed_demon'}
    bob_achieves = {
        'first_kill', 'level_10',
        'boss_slayer', 'collector'}
    charlie_achieves = {
        'level_10', 'treasure_hunter', 'boss_slayer',
        'speed_demon', 'perfectionist'}

    players = {
        'alice': alice_achieves,
        'bob': bob_achieves,
        'charlie': charlie_achieves
    }
    players = {player: set(achievs) for player, achievs in players.items()}

    for player, achieves in players.items():
        print(f"Player {player} achievements: {achieves}")
    print()

    print("=== Achievement Analytics ===")
    all_achieves = set.union(*players.values())
    print(f"All unique achievements: {all_achieves}")
    print(f"Total unique achievements: {len(all_achieves)}")
    print()

    common_achieves = set.intersection(*players.values())
    print(f"Common to all players: {common_achieves}")

    rare_achieves = set()
    for achieve in all_achieves:
        count = sum(1 for achieves in players.values() if achieve in achieves)
        if count == 1:
            rare_achieves.add(achieve)
    print(f"Rare achievements (1 player): {rare_achieves}")
    print()

    alice_bob_common = players['alice'].intersection(players['bob'])
    print(f"Alice vs Bob common: {alice_bob_common}")
    alice_unique = players['alice'].difference(players['bob'])
    print(f"Alice unique: {alice_unique}")
    bob_unique = players['bob'].difference(players['alice'])
    print(f"Bob unique: {bob_unique}")
    print()

    print("=== Missing Achievements ===")
    for player, achieves in players.items():
        missing = all_achieves.difference(achieves)
        print(f"{player} missing: {missing}")

    print()
    print("=== Player Communities ===")
    names = list(players.keys())
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            p1, p2 = names[i], names[j]
            shared = players[p1].intersection(players[p2])
            print(f"{p1} & {p2} shared: {shared}")

# Missing achievements: каждому игроку показывается, чего ему не хватает
# из общего набора.
# Communities: пары игроков и их общие достижения.


if __name__ == "__main__":
    ft_achievement_tracker()
