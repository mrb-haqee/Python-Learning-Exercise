def BMICalculator(gender: str, height: int) -> float:
    match gender:
        case "laki-laki":
            return (height-100)-((height-100)*0.1)
        case "perempuan":
            return (height - 100) - ((height - 100)*0.15)
    return 0.0  # TODO: replace this


# gunakan untuk melakukan debug
if __name__ == "__main__":
    print(BMICalculator("laki-laki", 165))
    print(BMICalculator("perempuan", 165))
