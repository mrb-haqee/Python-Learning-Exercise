def GraduateStudent(score: int, absent: int) -> str:
    if score>=70 and absent<5:
        return "lulus"
    return "tidak lulus"  # TODO: replace this


# gunakan untuk melakukan debug
if __name__ == "__main__":
    print(GraduateStudent(70, 4))
