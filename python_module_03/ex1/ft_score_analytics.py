#!/usr/bin/end python3
"""
Exercise 1: Score Analytics.

Collection theory: a list is a mutable container of values with stable order.
It supports append, iteration, and built-in aggregations like `sum`, `min`,
and `max`, making it a natural fit for numeric analytics.
"""

import sys


def ft_score_analytics() -> None:
    """Parse scores from CLI into a list and compute simple statistics."""
    print("=== Player Score Analytics ===")

    prog_name = sys.argv[0]
    if len(sys.argv) == 1:
        print(
            f"No scores provided. "
            f"Usage: python3 {prog_name} <score1> <score2> ...")
        return

    scores_list: list[int] = []

    for arg in sys.argv[1:]:
        try:
            score = int(arg)
            scores_list.append(score)
        except ValueError:
            print(
                f"Oops, u typed '{arg}' instead of a valid score. "
                "Skipping it.")

    if scores_list:
        total_players = len(scores_list)
        total_score = sum(scores_list)
        average_score = total_score / total_players
        max_score = max(scores_list)
        min_score = min(scores_list)
        score_range = max_score - min_score

        print(f"Scores processed: {scores_list}")
        print(f"Total players: {total_players}")
        print(f"Total score: {total_score}")
        print(f"Average score: {average_score}")
        print(f"High score: {max_score}")
        print(f"Low score: {min_score}")
        print(f"Score range: {score_range}")


if __name__ == "__main__":
    ft_score_analytics()
