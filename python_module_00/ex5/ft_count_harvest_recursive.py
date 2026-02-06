def ft_count_harvest_recursive(days: int | None = None) -> None:
    last_day = 0
    if (days is None):
        days = int(input("Days until harvest: "))
        last_day = 1
    if (days > 0):
        ft_count_harvest_recursive(days - 1)
        print(f"Day {days}")
    if (last_day):
        print("Harvest time!")

# 2nd version witt helper function in the main function
# def ft_count_harvest_recursive():
#    days = int(input("Days until harvest: "))
#    def helper(n):
#        if n == 0:
#            return
#        helper(n - 1)
#        print(f"Day {n}")
#    helper(days)
#    print("Harvest time!")

# 3rd version with helper function outside the main function
# def _count_days(n):
#    if n == 0:
#        return
#    _count_days(n - 1)
#    print(f"Day {n}")

# def ft_count_harvest_recursive():
#    days = int(input("Days until harvest: "))
#    _count_days(days)
#    print("Harvest time!")
