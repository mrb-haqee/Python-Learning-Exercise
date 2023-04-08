import datetime as dt
import os
import string as str
import random as rd

mahasiswa_template ={
    'nim':'nama',
    'nama':'0000000000',
    'lahir':dt.datetime(111,11,11),
    'sks_lulus':0,
    'beasiswa':True,
    'status_keaktifan':True,
    'nomer_hp':'000000000000'
}

data_mahasiswa ={}

while True:
    os.system("cls")
    print(f"{'SELAMAT DATANG DI PROGRAM PENGINPUTAN':^40}")
    print(f"{'DATA MAHASISWA':^40}")
    print("="*40)
    
    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    
    mahasiswa['nama'] = input("Nama Mahasiswa: ") #input nama
    mahasiswa['nim'] = input("NIM Mahasiswa: ") #input nim
    TAHUN_LAHIR = int(input("Tahun lahir (YYYY): ")) #input tahun
    BULAN_LAHIR = int(input("Bulan lahir (1-12): ")) #input bulan
    TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): ")) #input tgl
    mahasiswa['lahir'] = dt.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
    
    mahasiswa['sks_lulus'] = int(input("SKS Lulus: ")) #input sks
    mahasiswa['beasiswa'] = bool(int(input("Apakah Mendapatkan Beasiswa? (1/0): "))) #input beasiswa
    mahasiswa['status_keaktifan'] = bool(int(input("Status Keaktifan (1/0): "))) #status
    mahasiswa['nomer_hp'] = input("Nomer HP: ") #input nomerhp

    KEY = ''.join((rd.choice(str.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})

    print(f"\n{'KEY':<6} {'Nama':<30} {'NIM':<10} {'Tanggal Lahir':<15} {'SKS':^5} {'Beasiswa':^10} {'Status':^6} {'Nomer HP':^12}")
    print('-'*100)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
		
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']   
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
        SKS = data_mahasiswa[KEY]['sks_lulus']
        BEASISWA = data_mahasiswa[KEY]['beasiswa']
        STATUS = data_mahasiswa[KEY]['status_keaktifan']
        NOMERHP = data_mahasiswa[KEY]['nomer_hp']
        
        print(f"{KEY:<6} {NAMA:<30} {NIM:<10} {LAHIR:^15} {SKS:^5} {BEASISWA:^10} {STATUS:^6} {NOMERHP:<12}")
        # {STATUS:<10} {NOMERHP:<12} 
    
    
    
    
    
    
    
    
    
    Lanjut = input("Input lagi?(y/n)")
    if Lanjut == 'y':
        continue
    else:
        break
