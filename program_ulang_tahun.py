import datetime as dt
print("Selamat Datang di Birthday Machine".center(50,'='),'\n')

data_nama = input("Masukkan Nama: ")
data_tanggal = int(input("\n*Pakai angka semua ya!!\nMasukkan tanggal lahir : "))
data_bulan = int(input("Masukkan bulan lahir : "))
data_tahun = int(input("Masukkan tahun lahir : "))

# data_tanggal = 10
# data_bulan = 10
# data_tahun = 2005
hari_ini = dt.date.today()
data_lahir = dt.date(data_tahun, data_bulan, data_tanggal)

usia = hari_ini - data_lahir
usia_tahun = usia.days // 365
usia_bulan = (usia.days % 365)//30
usia_hari = (usia.days % 365 % 30)
print(f"\nManusia bernama {data_nama} lahir pada {data_lahir} hari {data_lahir:%A}.\n")
print(f"Pada Hari ini, tanggal {hari_ini}, hari {hari_ini:%A}")
print(f"Usia kamu adalah : {usia_tahun} tahun, {usia_bulan} bulan, {usia_hari} hari")

ulang_tahun = dt.date(hari_ini.year, data_bulan, data_tanggal)
pesta_ulang_tahun = ulang_tahun - hari_ini
if (pesta_ulang_tahun.days>0):
    print(f"Ulang tahunmu kurang {pesta_ulang_tahun.days} hari", end="")
    print(f"Atau {pesta_ulang_tahun.days//30} bulan, {pesta_ulang_tahun.days % 12} hari lagi")
elif(pesta_ulang_tahun.days<0):
    ulang_tahun = dt.date(hari_ini.year+1, data_bulan, data_tanggal)
    pesta_ulang_tahun2 = ulang_tahun - hari_ini
    print(f"Ulang tahunmu kurang {pesta_ulang_tahun2.days} hari ")
    print(f"Atau {pesta_ulang_tahun2.days//30} bulan, {pesta_ulang_tahun2.days % 12} hari lagi")






