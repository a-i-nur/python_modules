#!/usr/bin/env python3


import sys


def get_inventory_from_args(args: list[str]) -> dict[str, int] | None:
    inventory: dict[str, int] = {}
    for arg in args:
        try:
            parts = arg.split(":")
            if len(parts) != 2:
                raise ValueError(f"Invalid input. {arg}. "
                                 "Usage: item_name:quantity")
            item_name, quantity_str = parts
            quantity = int(quantity_str)
            if quantity < 0:
                raise ValueError(f"Invalid input: {arg}. "
                                 "Quantity must be >= 0")
            inventory[item_name] = inventory.get(item_name, 0) + quantity
        except ValueError as e:
            print(f"Error! {e}")
            return None
    return inventory


def get_units_str(quantity: int) -> str:
    if quantity == 1:
        return "unit"
    else:
        return "units"


def display_sorted_current_inventory(
        inventory: dict[str, int],
        total_items: int) -> None:

    percentages: dict[str, float] = {}
    printed: dict[str, int] = {}

    for item, quantity in inventory.items():
        percentage: float
        if total_items > 0:
            percentage = (quantity / total_items) * 100
        else:
            percentage = 0
        percentages.update({item: percentage})

    while len(printed) < len(inventory):
        max_item: str = ""
        for item, percentage in percentages.items():
            if item not in printed:
                if max_item == "" or percentage > percentages[max_item]:
                    max_item = item
        units_str = get_units_str(inventory[max_item])
        print(f"{max_item}: {inventory[max_item]} {units_str} "
              f"({percentages[max_item]:.1f}%)")
        printed.update({max_item: inventory[max_item]})


def display_inventory_statistics(inventory: dict[str, int]) -> None:
    most_abundant_item: str = ""
    for name, quantity in inventory.items():
        if most_abundant_item == "" \
                or quantity > inventory[most_abundant_item]:
            most_abundant_item = name
    least_abundant_item: str = ""
    for name, quantity in inventory.items():
        if least_abundant_item == "" \
                or quantity < inventory[least_abundant_item]:
            least_abundant_item = name
    units_str: str = get_units_str(inventory[most_abundant_item])
    print(f"Most abundant: {most_abundant_item} "
          f"({inventory[most_abundant_item]} {units_str})")
    units_str = get_units_str(inventory[least_abundant_item])
    print(f"Least abundant: {least_abundant_item} "
          f"({inventory[least_abundant_item]} {units_str})")


def display_item_categories(inventory: dict[str, int]) -> None:
    categories: dict[str, dict[str, int]] = {
        "abundant": {},
        "moderate": {},
        "scarce": {}
    }
    for name, quantity in inventory.items():
        if quantity > 10:
            categories["abundant"][name] = quantity
        elif quantity >= 4 and quantity <= 10:
            categories["moderate"][name] = quantity
        else:
            categories["scarce"][name] = quantity
    print(f"Abundant: {categories['abundant']}")
    print(f"Moderate: {categories['moderate']}")
    print(f"Scarce: {categories['scarce']}")


def get_last_item(inventory: dict[str, int]) -> str:
    last_item: str = ""
    for item in inventory.keys():
        last_item = item
    return last_item


def display_management_suggestions(inventory: dict[str, int]) -> None:
    restock_needed: dict[str, int] = {}
    for name, quantity in inventory.items():
        if quantity < 2:
            restock_needed[name] = quantity
    last_item: str = get_last_item(restock_needed)
    if restock_needed:
        print("Restock needed: ", end="")
        for item in restock_needed.keys():
            print(f"{item}", end="")
            if item != last_item:
                print(", ", end="")
        print()
    else:
        print("No restock needed.")


def ft_inventory_system() -> None:

    if len(sys.argv) == 1:
        print("Usage: python3 ft_inventory_system.py item:quantity ...")
        return

    inventory: dict[str, int] | None = get_inventory_from_args(sys.argv[1:])
    if inventory is None:
        return

    print("=== Inventory System Analysis ===")
    total_items: int = 0
    for quantity in inventory.values():
        total_items += quantity
    unique_items: int = len(inventory)
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_items}")
    print()

    print("=== Current Inventory ===")
    display_sorted_current_inventory(inventory, total_items)
    print()

    print("=== Inventory Statistics ===")
    display_inventory_statistics(inventory)
    print()

    print("=== Item Categories ===")
    display_item_categories(inventory)
    print()

    print("=== Management Suggestions ===")
    display_management_suggestions(inventory)
    print()

    print("=== Dictionary Properties Demo ===")
    print("Dictionary keys: ", end="")
    last_item = get_last_item(inventory)
    for item in inventory.keys():
        print(f'{item}', end="")
        if item != last_item:
            print(", ", end="")
    print()

    print("Dictionary values: ", end="")
    for item, quantity in inventory.items():
        print(f'{quantity}', end="")
        if item != last_item:
            print(", ", end="")
    print()

    print(f"Sample lookup - 'sword' in inventory: "
          f"{inventory.get('sword') is not None}")
    # print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


if __name__ == "__main__":
    ft_inventory_system()
