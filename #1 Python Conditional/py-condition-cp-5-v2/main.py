def TicketPlayground(height: int, age: int) -> int:
    if age > 12:
        return 100_000
    elif age == 12 or height > 160:
        return 60_000
    elif age >= 10 or height > 150:
        return 40_000
    elif age >= 8 or height > 135:
        return 25_000
    elif age >= 5 or height > 120:
        return 15_000
    elif age < 5:
        return -1


# return 0  # TODO: replace this

# gunakan untuk melakukan debug
if __name__ == "__main__":
    print(TicketPlayground(140, 13))
