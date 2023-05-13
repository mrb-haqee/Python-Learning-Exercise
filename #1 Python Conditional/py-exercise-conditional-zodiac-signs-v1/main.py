def zodiacSign(day: int, month: str) -> str:
    if day < 1 or day > 31:
        return "Input tanggal salah"
    else:
        if month == "Januari":
            if day >= 1 and day <= 19:
                return "Capricorn"
            elif day >= 20 and day <= 31:
                return "Aquarius"
        elif month == "Februari":
            if day >= 1 and day <= 18:
                return "Aquarius"
            elif day >= 19 and day <= 29:
                return "Pisces"
            else:
                return "Input tanggal salah"
        elif month == "Maret":
            if day >= 1 and day <= 20:
                return "Pisces"
            elif day >= 21 and day <= 31:
                return "Aries"
        elif month == "April":
            if day >= 1 and day <= 19:
                return "Aries"
            elif day >= 20 and day <= 30:
                return "Taurus"
        elif month == "Mei":
            if day >= 1 and day <= 20:
                return "Taurus"
            elif day >= 21 and day <= 31:
                return "Gemini"
        elif month == "Juni":
            if day >= 1 and day <= 20:
                return "Gemini"
            elif day >= 21 and day <= 30:
                return "Cancer"
        elif month == "Juli":
            if day >= 1 and day <= 22:
                return "Cancer"
            elif day >= 23 and day <= 31:
                return "Leo"
        elif month == "Agustus":
            if day >= 1 and day <= 22:
                return "Leo"
            elif day >= 23 and day <= 31:
                return "Virgo"
        elif month == "September":
            if day >= 1 and day <= 22:
                return "Virgo"
            elif day >= 23 and day <= 30:
                return "Libra"
        elif month == "Oktober":
            if day >= 1 and day <= 22:
                return "Libra"
            elif day >= 23 and day <= 31:
                return "Scorpio"
        elif month == "November":
            if day >= 1 and day <= 21:
                return "Scorpio"
            elif day >= 22 and day <= 30:
                return "Sagittarius"
        elif month == "Desember":
            if day >= 1 and day <= 21:
                return "Sagittarius"
            elif day >= 22 and day <= 31:
                return "Capricorn"
        else:
            return "Nama bulan salah"
    # return ""  # TODO: replace this


# gunakan untuk melakukan debug
if __name__ == "__main__":
    print(zodiacSign(22, "November"))
    print(zodiacSign(31, "Desember"))
    print(zodiacSign(41, "Desember"))
    print(zodiacSign(31, "Februari"))
    print(zodiacSign(29, "Februari"))
    print(zodiacSign(29, "Januari"))
