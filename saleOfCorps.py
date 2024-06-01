import csv  # import csv
import os  # import modul os (cls)
from pathlib import Path  # import modul path
from datetime import datetime as tanggal  # import datetime untuk tanggal

#menu pertama
# tambah admin
def addAdmin():
    os.system('cls') # membersihkan terminal
    with open('dataAdmin.csv', 'a', newline='') as file: #membuka file dataAdmin dengan akses a
        csvTambah = csv.writer(file)
        name = input("Masukkan Username : ") #menerima inputan nama admin
        password = input("Masukkan Password : ") #menerima inputan password
        csvTambah.writerow(
            [name, password])  #menambahkan ke csv nama dan password
        file.close() #menutup file csv
        os.system('cls')
        print("Data Berhasil ditambahkan!! \n")
        input("\n\nenter untuk lanjutkan")
        menuAwal() #kembali ke menu awal
        os.system('cls')

 
def login():
    os.system('cls')
    nama = input("masukkan nama : ") #menerima inputan nama
    password = input("masukkan password : ") # menerima inputan password
    user = [] #membuat list kosongan untuk menampung isi dari dataAdmin
    with open("dataAdmin.csv", 'r') as file: # membuka file dataAdmin dengan akses read
        csvreader = csv.reader(file) 
        for row in csvreader: # perulangan untuk memasukkan data admin ke list user
            user.append(row) # memasukkan setiap barisnya ke list user
    indeks = 0 #indeks dimulai dari 0
    for i in range(len(user)-1): # membuat perulangan data user dengan jumlah baris -1
        indeks += 1 # setiap melewati 1 perulangan indeks ditambahkan 1
        if (user[indeks][0] == nama) and (user[indeks][1] == password): #pengecekan apakah nama yang diinputkan sama dengan nama dari dataAdmin dan password yang diinputkan sama dengan password dataAdmin
            pilihMenu()
    menuAwal()

def adminHead(judul):
    with open('dataAdmin.csv', 'w', newline='') as filecsv: #membuka file dataAdmin dengan akses write
        tulis = csv.DictWriter(filecsv, fieldnames=judul,  delimiter=',') # membuat judul yang dipisahkan koma
        tulis.writeheader()

def menuAwal():
    os.system('cls')
    print('='*39)
    print("======== Sale Of Corps ========")
    print('='*39)
    print('-'*13, 'Daftar Menu', '-'*13)
    print('[1] Sign-up \n[2] Sign-in \n[3] Exit')
    print('='*39)
    pilih = int(input('pilih menu : ')) #inputan menu 
    if pilih == 1: #ketika pilih 1 akan menjalankan adminHead dan addAdmin
        if not(Path('dataAdmin.csv').is_file()): # pengecekan ketika tidak ada file dataAdmin akan menjalankan fungsi adminHead
            adminHead(["Nama", "Password"])
        addAdmin()
    elif pilih == 2: #ketika pilih 2 akan menjalankan fungsi login
        login()
    elif pilih == 3: # ketika pilih 3 akan keluar aplikasi
        os.system('cls')
        print("Terima Kasih!!")
        exit()
    else: # ketika semua pengecekan tidak terpenuhi akan tetap di menu awal
        menuAwal()

def pilihMenu():
    os.system('cls')
    print('='*39)
    print("======== Sale Of Corps ========")
    print('='*39)
    print('-'*13, 'Daftar Menu', '-'*13)
    print('[1] mengelola Data sayur \n[2] mengelola data transaksi \n[3] logout ')
    print('='*39)
    menu = int(input("Masukkan nomor menu : ")) 
    if menu == 1:
        tampilMenu()
    elif menu == 2:
        aksi()
    elif menu == 3:
        menuAwal()
    else:
        pilihMenu()

#menu sayur

def getSayur():
    os.system('cls')
    rows = [] #membuat list kosongan untuk menampung dataSayur 
    with open("dataSayur.csv", 'r') as file: #membuka dataSayur dengan akses Read
        csvreader = csv.reader(file)
        for row in csvreader:
            rows.append(row)
        judul = rows.pop(0)
        judul.insert(0, 'No')  # menambahkan 'no' di index pertama judul
        no = 1  # no diwalai dari 1
        print('='*103)
    print('='*40, 'Seluruh Data sayur', '='*41)
    print('='*103)
    # print judul
    print(
        f"{judul[0]}\t {judul[1]} \t\t {judul[2]} \t {judul[3]}")
    print('-'*103)
    for i in rows:
        print(
            f"{no}\t{i[0]} \t\t {i[1]} \t {i[2]} ")
        no += 1
    file.close()


def tampilSayur():
    getSayur()
    print('='*103)
    input("Enter Untuk Kembali!!")
    os.system('cls')
    tampilMenu()


def addSayur():
    os.system('cls')
    with open('dataSayur.csv', 'a', newline='') as file:
        csvTambah = csv.writer(file)
        print('='*31)
        print("="*9, 'Tambah Data Sayur', '='*9)
        print('='*31)
        namaSayur = input("nama sayur : ")
        harga = input("harga : ")
        stok = input("stok : ")
        csvTambah.writerow(
            [namaSayur, harga, stok])
        file.close()
        os.system('cls')
        print("Data Berhasil Diinput!!! \n")
        print('\n===================================',
              "\nnama sayur         : ", namaSayur,
              "\nharga              : ", harga,
              '\nstok               : ', stok,
              '\n===================================\n')
        input("\n\nenter untuk lanjutkan")
        os.system('cls')
        tampilMenu()


def editSayur():
    getSayur()  # menampilkan data sayur
    print("-"*103)
    rows = []  # membuat list kosong untuk diisi data csv
    with open("dataSayur.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:  # perulangan untuk mengambil data setiap barisnya di csv
            rows.append(row)  # menambahkan data dari csv ke list row
    # inputan untuk memilih baris yang akan diedit
    
    edit = int(input("Pilih nomor : "))
    if edit > len(rows) or 0:  # ketika user menginputkan angka yang tidak ada
        print("inputan salah")
        input("enter")
        editSayur()

    namaSayur = input("nama sayur : ")
    harga = int(input("harga : "))
    stok = int(input("stok : "))
    indeks = 0
    for data in range(len(rows)):
        if data == edit:
            rows[indeks][0] = namaSayur
            rows[indeks][1] = harga
            rows[indeks][2] = stok
        indeks += 1

    judul = rows.pop(0)
    with open("dataSayur.csv", "w", newline="") as file:
        tulis = csv.DictWriter(file, fieldnames=judul)  # menambahkan header
        tulis.writeheader()
        for data in rows:
            tulis.writerow(
                {'Nama_sayur': data[0], 'Harga': data[1], 'Stok': data[2]})
    print("Data berhasil diubah !!!\n")
    input("Enter Untuk Kembali !!")
    tampilMenu()


def deleteSayur():
    getSayur()
    print("-"*103)
    
    rows = []
    with open("dataSayur.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            rows.append(row)

    hps = int(input("hapus nomor : "))
    indeks = 0
    for data in range(len(rows)):
        if data == hps:  # ketika data bernilai sama dengan variable hps
            rows.remove(rows[indeks])  # menghapus list di index yang dituju
        indeks += 1

    judul = rows.pop(0)
    with open("dataSayur.csv", "w", newline="") as file:
        tulis = csv.DictWriter(file, fieldnames=judul)
        tulis.writeheader()
        for data in rows:
            tulis.writerow(
                {'Nama_sayur': data[0], 'Harga': data[1], 'Stok': data[2]})
    print("Data berhasil dihapus !!!\n")
    input("Enter Untuk Kembali !!")
    tampilMenu()

# fungsi untuk membuat header di csv data sayur
def createHeader(judul):
    with open('dataSayur.csv', 'w', newline='') as filecsv:
        tulis = csv.DictWriter(filecsv, fieldnames=judul,  delimiter=',')
        tulis.writeheader()




#Menu Transaksi
def getTransaksi():
    os.system('cls')
    rows = []
    with open("dataTransaksi.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            rows.append(row)
        judul = rows.pop(0)
        judul.insert(0, 'No')  # menambahkan 'no' di index pertama judul
        no = 1  # no diwalai dari 1
        print('='*103)
    print('='*40, 'Seluruh Data Transaksi', '='*41)
    print('='*103)
    # print judul
    print(
        f"{judul[0]}\t {judul[1]} \t\t {judul[2]} \t {judul[3]} \t {judul[4]} \t {judul[5]}")
    print('-'*103)
    for i in rows:
        print(
            f"{no}\t{i[0]} \t\t {i[1]} \t\t {i[2]} \t {i[3]} \t\t {i[4]}")
        no += 1
    file.close()
    print('='*103)
    input("Enter Untuk Kembali!!")
    os.system('cls')
    aksi()


def addTransaksi():
    getSayur()
    print("-"*103)
    rows = [] # membuat list kosongan yang akan berisi data sayur
    dibeli = [] # membuat list kosongan yang akan berisi data yang akan dibeli
    trans = [] # membuat list kosongan yang akan berisi data yang akan ditambahkan di data transaksi
    with open("dataSayur.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader: 
            rows.append(row)
    beli = int(input("pilih nomor yang dibeli : ")) 
    if beli > len(rows):  # ketika user menginputkan angka yang tidak ada
        print("inputan salah") 
        input("enter")
        addTransaksi()

    for data in range(len(rows)): #menambahkan data sayur yang dipilih ke list dibeli
        if data == beli:
            dibeli.append(rows[data][0])
            dibeli.append(rows[data][1])
            dibeli.append(rows[data][2])
    jumlah = int(input("jumlah beli :"))
    uangBayar = int(input("uang bayar : "))
    tgl = tanggal.now()
    tgl_tr = (str(tgl.day) + '/' +
              str(tgl.month) + '/' + str(tgl.year))  # menyimpan waktu hari ini secara detail
    namaSayur = dibeli[0] 
    harga = int(dibeli[1])
    total = jumlah * harga
    uangKembali = uangBayar - total
    stok = int(dibeli[2])
    sisaStok = stok - jumlah
    # mengurangi stok di data sayur
    indeks = 0
    for data in range(len(rows)):
        if data == beli:
            rows[indeks][0] = dibeli[0]
            rows[indeks][1] = dibeli[1]
            rows[indeks][2] = sisaStok
        indeks += 1
    judul = rows.pop(0)
    with open("dataSayur.csv", "w", newline="") as file:
        tulis = csv.DictWriter(file, fieldnames=judul)  # menambahkan header
        tulis.writeheader()
        for data in rows:
            tulis.writerow(
                {'Nama_sayur': data[0], 'Harga': data[1], 'Stok': data[2]})

    file.close()
    trans.append(tgl_tr)
    trans.append(namaSayur)
    trans.append(total)
    trans.append(uangBayar)
    trans.append(uangKembali)

    if not(Path('dataTransaksi.csv').is_file()):
        headTrans(["tgl_transaksi", "barang", "total",
                  "uang_bayar", "uang_kembali"])
    transaksi(trans)

    print("\nBerhasil input transaksi")
    input("\nenter untuk lanjutkan")
    os.system('cls')
    aksi()


def transaksi(trans):
    with open('dataTransaksi.csv', 'a', newline='') as file:
        csvTambah = csv.writer(file)
        transaksi = trans
        csvTambah.writerow(
            [transaksi[0], transaksi[1], transaksi[2], transaksi[3], transaksi[4]])


def aksi():
    os.system('cls')
    print('='*39)
    print("======== Sale Of Corps ========")
    print('='*39)
    print('-'*13, 'Daftar Menu', '-'*13)
    print('[1] Data transaksi \n[2] Tambah transaksi \n[3] Keluar')
    print('='*39)
    menu = int(input("Masukkan nomor menu : "))
    if menu == 1:
        getTransaksi()
    elif menu == 2:

        addTransaksi()
    elif menu == 3:
        pilihMenu()
    else:
        aksi()

def headTrans(judul):
    with open('dataTransaksi.csv', 'w', newline='') as filecsv:
        tulis = csv.DictWriter(filecsv, fieldnames=judul,  delimiter=',')
        tulis.writeheader()

def tampilMenu():
    os.system('cls')
    print('='*39)
    print("======== Sale Of Corps ========")
    print('='*39)
    print('-'*13, 'Daftar Menu', '-'*13)
    print('[1] Tampil data \n[2] Tambah data \n[3] Ubah data \n[4] Hapus data \n[5] Keluar')
    print('='*39)
    menu = int(input("Masukkan nomor menu : "))
    if menu == 1:
        tampilSayur()
    elif menu == 2:
        if not(Path('dataSayur.csv').is_file()):
            createHeader(["Nama_sayur", "Harga", "Stok"])
        addSayur()
    elif menu == 3:
        editSayur()
    elif menu == 4:
        deleteSayur()
    elif menu == 5:
        pilihMenu()
    else:
        tampilMenu()



if __name__ == "__main__":
    menuAwal()
