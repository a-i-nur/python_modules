#!/usr/bin/env python3
"""
Exercise 6: Data Alchemist (Comprehensions Dashboard).

Collection theory: list comprehensions transform ordered sequences,
dict comprehensions build key-value mappings, and set comprehensions
produce unique, unordered values. They are concise, readable tools for
filtering, grouping, and deduplicating data.
"""


def ft_analytics_dashboard() -> None:
    """Print a small analytics report using list/dict/set comprehensions."""
    # Sample gaming data (keep it simple and in-memory)
    players = [
        {
            "name": "alice",
            "score": 2300,
            "achievements": ["first_kill", "level_10", "boss_slayer"],
            "region": "north",
        },
        {
            "name": "bob",
            "score": 1800,
            "achievements": ["first_kill", "level_5"],
            "region": "east",
        },
        {
            "name": "charlie",
            "score": 2150,
            "achievements": ["level_10", "boss_slayer", "speed_runner"],
            "region": "central",
        },
        {
            "name": "diana",
            "score": 2100,
            "achievements": ["first_kill", "level_10"],
            "region": "north",
        },
    ]

    print("=== Game Analytics Dashboard ===")

    # List Comprehension Examples
    print("=== List Comprehension Examples ===")
    high_scorers = [
        player["name"] for player in players if player["score"] > 2000
    ]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [player["score"] * 2 for player in players]
    print(f"Scores doubled: {scores_doubled}")

    active_players = [
        player["name"]
        for player in players
        if len(player["achievements"]) > 2
    ]
    print(f"Active players: {active_players}")

    # Dict Comprehension Examples
    print("=== Dict Comprehension Examples ===")
    player_scores = {player["name"]: player["score"] for player in players}
    print(f"Player scores: {player_scores}")

    category_labels = ["high", "medium", "low"]
    score_categories = {
        label: sum(
            1
            for player in players
            if (
                (label == "high" and player["score"] > 2000)
                or (label == "medium" and 1500 < player["score"] <= 2000)
                or (label == "low" and player["score"] <= 1500)
            )
        )
        for label in category_labels
    }
    print(f"Score categories: {score_categories}")

    achievement_counts = {
        player["name"]: len(player["achievements"]) for player in players
    }
    print(f"Achievement counts: {achievement_counts}")

    # Set Comprehension Examples
    print("=== Set Comprehension Examples ===")
    unique_players = {player["name"] for player in players}
    print(f"Unique players: {unique_players}")
    unique_achievements = {
        achievement
        for player in players
        for achievement in player["achievements"]
    }
    print(f"Unique achievements: {unique_achievements}")
    active_regions = {
        player["region"]
        for player in players
        if len(player["achievements"]) > 2
    }
    print(f"Active regions: {active_regions}")

    # Combined Analysis
    print("=== Combined Analysis ===")
    total_players = len(players)
    total_unique_achievements = len(unique_achievements)
    average_score = sum(player["score"] for player in players) / total_players
    top_performer = max(players, key=lambda p: p["score"])
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score:.2f}")
    print(
        "Top performer: "
        f"{top_performer['name']} ({top_performer['score']} points, "
        f"{len(top_performer['achievements'])} achievements)"
    )


if __name__ == "__main__":
    try:
        ft_analytics_dashboard()
    except (KeyError, TypeError, ZeroDivisionError) as exc:
        print(f"Error: {exc}")
