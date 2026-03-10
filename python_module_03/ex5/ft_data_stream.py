#!/usr/bin/env python3


import typing


def event_stream(num_events: int) -> typing.Generator[tuple, None, None]:
    """Yield event tuples without storing the whole dataset."""
    players: list[str] = ["alice", "bob", "charlie", "diana", "eve"]
    actions: list[str] = [
        "killed monster",
        "found treasure",
        "leveled up",
        "completed quest",
    ]
    levels: list[int] = [5, 12, 8, 15, 3]

    for i in range(num_events):
        event_id = i + 1
        player = players[i % len(players)]
        action = actions[i % len(actions)]
        level = levels[i % len(levels)]
        yield (event_id, player, level, action)


def batch_event_stream(
        num_events: int,
        batch_size: int) -> typing.Generator[list[tuple], None, None]:
    """Yield game events in fixed-size batches."""
    batch: list[tuple] = []
    for event in event_stream(num_events):
        batch.append(event)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch


def fibonacci_stream(n: int) -> typing.Generator[int, None, None]:
    """Yield the first n Fibonacci numbers, one by one."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# def fibonacci_stream(n: int) -> list[int]:
#     """List of the first n Fibonacci numbers, one by one."""
#     fib_list: list[int] = []
#     a, b = 0, 1
#     for _ in range(n):
#         fib_list.append(a)
#         a, b = b, a + b
#     return fib_list


def prime_stream(n: int) -> typing.Generator[int, None, None]:
    """Yield the first n prime numbers, one by one."""
    count = 0
    num = 2
    while count < n:
        is_prime = True
        divisor = 2
        while divisor * divisor <= num:
            if num % divisor == 0:
                is_prime = False
                break
            divisor += 1
        if is_prime:
            yield num
            count += 1
        num += 1


def ft_data_stream() -> None:
    """Run a demo: stream events, compute stats, and show generators."""
    print("=== Game Data Stream Processor ===")
    print()

    num_events: int = 1000
    print(f"Processing {num_events} game events...")
    print()

    for event_id, player, level, action in event_stream(num_events):
        if event_id > 3:
            break
        print(f"Event {event_id}: Player {player} (level {level}) {action}")
    print("...")
    print()

    print("=== Stream Analytics ===")
    print(f"Total events processed: {num_events}")
    high_level_players: int = 0
    treasure_events: int = 0
    level_up_events: int = 0
    batch_size = 100
    batches_processed: int = 0
    for batch in batch_event_stream(num_events, batch_size):
        batches_processed += 1
        for _, _, level, action in batch:
            if level >= 10:
                high_level_players += 1
            if action == "found treasure":
                treasure_events += 1
            if action == "leveled up":
                level_up_events += 1

    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print(f"Batches processed ({batch_size}/batch): {batches_processed}")
    print()

    print("=== Store vs Stream ===")
    stored_events = []
    for event in event_stream(num_events):
        stored_events.append(event)
    print(f"Stored events in list: {len(stored_events)}")
    print("Memory usage: High (O(n)) (stored list)")

    streamed_count = 0
    for _ in event_stream(num_events):
        streamed_count += 1
    print(f"Streamed events count: {streamed_count}")
    print("Memory usage: Constant (O(1)) (streaming)")
    print()

    num_fib: int = 10
    print("=== Generator Demonstration ===")
    print(f"Fibonacci sequence (first {num_fib}): ", end="")
    fib_iter = iter(fibonacci_stream(num_fib))
    first_num = next(fib_iter, None)
    if first_num is not None:
        print(first_num, end="")
    while True:
        num = next(fib_iter, None)
        if num is None:
            break
        print(f", {num}", end="")
    print()

    num_primes: int = 5
    print(f"Prime numbers (first {num_primes}): ", end="")
    prime_iter = iter(prime_stream(num_primes))
    first_num = next(prime_iter, None)
    if first_num is not None:
        print(first_num, end="")
    while True:
        num = next(prime_iter, None)
        if num is None:
            break
        print(f", {num}", end="")
    print()


if __name__ == "__main__":
    ft_data_stream()
