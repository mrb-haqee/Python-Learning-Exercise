# Latihan program sederhana
list_buku =[]
while True:
    print("\nInput Buku")
    judul = input("Judul Buku\t: ")
    penulis = input("Penulis Buku\t: ")
    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)
    
    print("\n\n","Data Buku".center(20,"="))
    print(f"No.| Judul\t | Penulis")
    for index,buku in enumerate(list_buku):
        print(f"{index+1}. | {buku[0]}\t | {buku[1]}")
    
    print("="*20)
    Lanjut = input("Apakah ingin di lanjutkan? (y/n)")
    if Lanjut == "n":
        break
    elif Lanjut == "y":
        continue
    else:
        break
    
print("PROGRAM SELESAI")