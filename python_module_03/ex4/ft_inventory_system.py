#!/usr/bin/env python3
"""
Exercise 4: Inventory System.

Collection theory: dictionaries map keys to values and provide fast lookup.
They preserve insertion order, which helps create stable reports. Nested
dicts can model structured records like inventory items and stats.
"""

import sys


def parse_quantity(s: str):
    """Parse a non-negative integer; return None on invalid input."""
    digits = {
        "0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
        "5": 5, "6": 6, "7": 7, "8": 8, "9": 9
    }
    if len(s) == 0:
        return None
    total = 0
    for ch in s:
        d = digits.get(ch)
        if d is None:
            return None
        total = total * 10 + d
    return total


def print_comma_separated(iterable):
    """Print iterable items separated by comma and space on a single line."""
    first = True
    for x in iterable:
        if not first:
            print(", ", end="")
        print(x, end="")
        first = False
    print()


def percent_one_decimal(quantity, total):
    """Compute percentage as (int_part, frac) for one decimal place."""
    if total == 0:
        return 0, 0
    percent10 = (quantity * 1000 + (total // 2)) // total
    int_part = percent10 // 10
    frac = percent10 - int_part * 10
    return int_part, frac


def ft_inventory_system() -> None:
    """Parse CLI inventory into dicts and print a structured report.

    Input: argv items formatted as name:quantity.
    Output: a fixed report with totals, sorted inventory, stats, categories,
    suggestions, and dictionary method demos as required by the subject.
    """
    if len(sys.argv) < 2:
        print(
            "Usage: python3 ft_inventory_system.py "
            "item1:quantity1 item2:quantity2 ..."
        )
        return

    inventory = {}
    inventory_details = {}

    for arg in sys.argv[1:]:
        parts = arg.split(":")
        if len(parts) != 2:
            print("Invalid input:", arg, ". Expected format 'item:quantity'.")
            return
        name = parts[0]
        quantity = parse_quantity(parts[1])
        if quantity is None:
            print("Invalid input:", arg, ". Expected numeric quantity.")
            return

        current_qty = inventory.get(name)
        if current_qty is None:
            inventory.update({name: quantity})
        else:
            inventory.update({name: current_qty + quantity})

        detail = inventory_details.get(name)
        if detail is None:
            detail = {
                "name": name,
                "type": "unknown",
                "quantity": 0,
                "value": 0,
            }
            inventory_details.update({name: detail})
        detail.update({"quantity": detail.get("quantity") + quantity})

    total_items = 0
    for qty in inventory.values():
        total_items = total_items + qty

    print("=== Inventory System Analysis ===")
    print("Total items in inventory:", total_items)
    print("Unique item types:", len(inventory))

    print("=== Current Inventory ===")
    remaining = dict(inventory)
    ordered = {}
    while len(remaining) > 0:
        max_name = None
        max_qty = None
        for name, qty in remaining.items():
            if max_name is None or qty > max_qty:
                max_name = name
                max_qty = qty
        ordered.update({max_name: max_qty})
        del remaining[max_name]

    for name, qty in ordered.items():
        int_part, frac = percent_one_decimal(qty, total_items)
        if qty == 1:
            unit_label = "unit"
        else:
            unit_label = "units"
        print(
            name,
            ": ",
            qty,
            " ",
            unit_label,
            " (",
            int_part,
            ".",
            frac,
            "%)",
            sep="",
        )

    if len(ordered) > 0:
        most_name = None
        most_qty = None
        least_name = None
        least_qty = None
        for name, qty in inventory.items():
            if most_name is None or qty > most_qty:
                most_name = name
                most_qty = qty
            if least_name is None or qty < least_qty:
                least_name = name
                least_qty = qty

        print("=== Inventory Statistics ===")
        if most_qty == 1:
            most_unit_label = "unit"
        else:
            most_unit_label = "units"
        if least_qty == 1:
            least_unit_label = "unit"
        else:
            least_unit_label = "units"
        print(
            "Most abundant: ",
            most_name,
            " (",
            most_qty,
            " ",
            most_unit_label,
            ")",
            sep="",
        )
        print(
            "Least abundant: ",
            least_name,
            " (",
            least_qty,
            " ",
            least_unit_label,
            ")",
            sep="",
        )

        categories = {"Moderate": {}, "Scarce": {}}
        for name, qty in inventory.items():
            if qty >= 5 and qty <= 10:
                categories.get("Moderate").update({name: qty})
            if qty < 5:
                categories.get("Scarce").update({name: qty})

        print("=== Item Categories ===")
        print("Moderate:", categories.get("Moderate"))
        print("Scarce:", categories.get("Scarce"))

        print("=== Management Suggestions ===")
        restock = {}
        for name, qty in inventory.items():
            if qty < 2:
                restock.update({name: 1})
        if len(restock) > 0:
            print("Restock needed:", end=" ")
            print_comma_separated(restock.keys())
        else:
            print("No restocking needed.")

    print("=== Dictionary Properties Demo ===")
    print("Dictionary keys:", end=" ")
    print_comma_separated(inventory.keys())
    print("Dictionary values:", end=" ")
    print_comma_separated(inventory.values())
    sample_item = "sword"
    print("Sample lookup - 'sword' in inventory:", sample_item in inventory)


if __name__ == "__main__":
    ft_inventory_system()
