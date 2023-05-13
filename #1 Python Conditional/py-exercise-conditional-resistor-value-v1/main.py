def resistorValue(bandColor1: str, bandColor2: str, bandColor3: str, bandColor4: str) -> str:
    color = {
        "black":  "0",
        "brown":  "1",
        "red":    "2",
        "orange": "3",
        "yellow": "4",
        "green":  "5",
        "blue":   "6",
        "violet": "7",
        "grey":   "8",
        "white":  "9",
    }
    significantFigure = ""
    for k, v in color.items():
        for k2, v2 in color.items():
            if bandColor1 == k and bandColor2 == k2:
                significantFigure = v + v2
    mult = 1
    for k in color:
        if bandColor3 == k:
            num = int(significantFigure)
            mult *= num
            break
        mult *= 10

    if bandColor4 == "black":
        return f"{mult} ohm ±20%"
    elif bandColor4 == "brown":
        return f"{mult} ohm ±1%"
    elif bandColor4 == "red":
        return f"{mult} ohm ±2%"
    elif bandColor4 == "gold":
        return f"{mult} ohm ±5%"
    else:
        return f"{mult} ohm ±10%"
    return ""  # TODO: replace this


# gunakan untuk melakukan debug
if __name__ == "__main__":
    print(resistorValue("black", "brown", "red", "gold"))
    print(resistorValue("red", "red", "red", "gold"))
    print(resistorValue("yellow", "violet", "green", "silver"))
    print(resistorValue("blue", "grey", "green", "silver"))
