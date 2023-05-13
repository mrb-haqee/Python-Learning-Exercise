def profitMonitor(todayProfit: int, lastProfit: int) -> str:
    if todayProfit>lastProfit:
        return f"Profit naik sebanyak {todayProfit-lastProfit} point"
    elif todayProfit<lastProfit:
        return f"Profit turun sebanyak {lastProfit-todayProfit} point"
    else:
        return "Profit stabil"  # TODO: replace this


# gunakan untuk melakukan debug
if __name__ == "__main__":
    print(profitMonitor(100, 50))
    print(profitMonitor(50, 100))
    print(profitMonitor(100, 100))
