def hollyKnight(name:str, stamina:int, undead:int)->str:
    if stamina>undead:
        return f"Holly Knight {name} memenangkan pertempuran dengan mudah!"
    elif stamina==undead:
        return f"Beruntung Holly knight {name} berhasil mengalahkan {undead} undead!"
    elif undead>stamina:
        return f"Holly knight {name} mengalahkan {stamina} undead, namun sayang holly knight {name} gugur di medan perang!"
        
    return "" # TODO: replace this

# gunakan untuk melakukan debug
if __name__ == "__main__":
    print(hollyKnight("Lancelot", 30, 20)) # Holly Knight Lancelot memenangkan pertempuran dengan mudah!
    print(hollyKnight("Gallahad", 10, 10)) # Beruntung Holly knight Gallahad berhasil mengalahkan 10 undead!
    print(hollyKnight("Tristan", 100, 110)) # Holly knight Tristan mengalahkan 100 undead, namun sayang holly knight Tristan gugur di medan perang!
