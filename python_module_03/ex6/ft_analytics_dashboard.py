#!/usr/bin/env python3


def ft_analytics_dashboard() -> None:
    """Print a small analytics report using list/dict/set comprehensions."""
    players: list[dict] = [
        {
            "name": "Aynur",
            "score": 2300,
            "achievements": ["vim using", "milestone 2", "piano_playing"],
            "region": "Tatarstan"
        },
        {
            "name": "Qaysar",
            "score": 1800,
            "achievements": ["vim using", "milestone 3"],
            "region": "Qazaqstan"
        },
        {
            "name": "Sveta",
            "score": 2150,
            "achievements": ["milestone 2", "piano_playing", "romanian"],
            "region": "Romania"
        },
        {
            "name": "Irek",
            "score": 2100,
            "achievements": ["vim using", "milestone 2"],
            "region": "Tatarstan"
        }]

    print("=== Game Analytics Dashboard ===")
    print()

    print("=== List Comprehension Examples ===")
    high_scorers = [
        player["name"] for player in players if player["score"] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [player["score"] * 2 for player in players]
    print(f"Scores doubled: {scores_doubled}")

    active_players = [
        player["name"]
        for player in players
        if len(player["achievements"]) > 2]
    print(f"Active players: {active_players}")
    print()

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
            ))
        for label in category_labels}
    print(f"Score categories: {score_categories}")

    achievement_counts = {
        player["name"]: len(player["achievements"]) for player in players}
    print(f"Achievement counts: {achievement_counts}")
    print()

    print("=== Set Comprehension Examples ===")
    unique_players = {player["name"] for player in players}
    print(f"Unique players: {unique_players}")
    unique_achievements = {
        achievement
        for player in players
        for achievement in player["achievements"]}
    print(f"Unique achievements: {unique_achievements}")
    active_regions = {
        player["region"]
        for player in players
        if len(player["achievements"]) > 2}
    print(f"Active regions: {active_regions}")
    print()

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
        f"{len(top_performer['achievements'])} achievements)")
    print()


if __name__ == "__main__":
    ft_analytics_dashboard()
