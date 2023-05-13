def mineralMining(mineral: str, miningPower: int, duration: int, cost: int) -> str:
    match mineral:
        case "gold":
            result = duration / 30 * miningPower * 1
            if result < cost:
                return f"Mineral mining at a loss {result-cost}"
            else:
                return f"Mineral mining profit {result-cost}"
        case "silver":
            result = round(duration / 20 * miningPower * 0.6)
            if result < cost:
                return f"Mineral mining at a loss {result-cost}"
            else:
                return f"Mineral mining profit {result-cost}"
        case "coper":
            result = duration / 5 * miningPower * 0.3
            if result < cost:
                return f"Mineral mining at a loss {result-cost}"
            else:
                return f"Mineral mining profit {result-cost}"
        case "uranium":
            result = duration / 75 * miningPower * 3
            if result < cost:
                return f"Mineral mining at a loss {result-cost}"
            else:
                return f"Mineral mining profit {result-cost}"
        case "platinum":
            result = duration / 15 * miningPower * 2
            if result < cost:
                return f"Mineral mining at a loss {result-cost}"
            else:
                return f"Mineral mining profit {result-cost}"
        case "titanium":
            result = duration / 55 * miningPower * 1.5
            if result < cost:
                return f"Mineral mining at a loss {result-cost}"
            else:
                return f"Mineral mining profit {result-cost}"
    return "Invalid mineral name"  # TODO: replace this


# gunakan untuk melakukan debug
if __name__ == "__main__":
    print(
        mineralMining("gold", 10, 70, 59)
    )  # Mineral mining at a loss -35.666666666666664
    print(mineralMining("rock", 10, 70, 40))  # Invalid mineral name
    print(mineralMining("uranium", 10, 70, 150))  # Mineral mining at a loss -122
    print(mineralMining("silver", 33, 200, 30))  # Mineral mining profit 168
    print(
        mineralMining("titanium", 25, 100, 200)
    )  # Mineral mining at a loss -131.8181818181818
    print(
        mineralMining("gold", 1, 100, 15)
    )  # Mineral mining at a loss -11.666666666666666
    print(
        mineralMining("titanium", 20, 350, 150)
    )  # Mineral mining at a loss 40.90909090909091
