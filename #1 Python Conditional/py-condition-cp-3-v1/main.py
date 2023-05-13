def GetPredicate(math: int, science: int, english: int, indonesia: int) ->str: 
    avg = (math + science + english + indonesia) / 4
    if avg == 100:
        return "Sempurna"
    elif avg >= 90:
        return "Sangat Baik"
    elif avg >= 80:
        return "Baik"
    elif avg >= 70:
        return "Cukup"
    elif avg >= 60:
        return "Kurang"
    elif avg < 60:
        return "Sangat kurang"  # TODO: replace this
    return ""


if __name__ == "__main__":
    print(GetPredicate(50, 80, 100, 60))
