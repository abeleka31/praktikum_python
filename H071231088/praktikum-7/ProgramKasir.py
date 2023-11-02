
import os
import random
from datetime import datetime

garis = "========================" * 4

if not os.path.exists("invoices"):
    os.makedirs("invoices")

def id_transaksi(kasir):
    now = datetime.now()
    id = kasir[:3].upper() + now.strftime("%y%m%d%H%M") + str(random.randint(100, 999))
    return id

def cetak_invoice(kasir, items):
    id_transaksi_invoice = id_transaksi(kasir)  # Menggunakan ID yang dihasilkan dari fungsi id_transaksi
    NamaFile = f"invoices/{id_transaksi_invoice}.txt"
    with open(NamaFile, "w") as file:
        spasi = "       "
        kata = "TOKOH " + kasir.upper()
        now = datetime.now()
        file.write(f"{spasi*6}{kata} \n")
        file.write(f"{garis} \n")
        file.write(f"Nama Kasir: {kasir} \n")
        file.write(f"Tanggal Transaksi: {now.strftime('%d/%m/%Y %H:%M')}\n")
        file.write(f"{garis} \n")
        file.write(f"{spasi*6} DAFTAR PRODUK\n")
        garis_kolom = "=====================" * 4
        file.write(f"{spasi}{garis_kolom}\n")
        file.write(f"{spasi}|       NAMA        |       HARGA       |       JUMLAH       |      TOTAL          |\n")
        file.write(f"{spasi}{garis_kolom}\n")
        total_harga = 0
        for item in items:
            nama_produk, harga, jumlah = item
            nama_produk = ((nama_produk[:10] + "...") if len(nama_produk) > 10 else nama_produk).ljust(10)
            harga = str(harga)
            harga = ((harga[:10] + "...") if len(harga) > 10 else harga).ljust(10)
            int_harga = int(harga)
            jumlah = str(jumlah)
            jumlah = ((jumlah[:10] + "...") if len(jumlah) > 10 else jumlah).ljust(10)
            int_jumlah = int(jumlah)
            subtotal = int_harga * int_jumlah
            total_harga += subtotal
            subtotal_1 = str(subtotal)
            subtotal_1 = ((subtotal_1[:10] + "...") if len(subtotal_1) > 10 else subtotal_1).ljust(10)
            total_harga_1 = str(total_harga)
            total_harga_1 = ((total_harga_1[:10] + "...") if len(total_harga_1) > 10 else total_harga_1).ljust(10)
            file.write(f"{spasi}| {nama_produk}        | Rp.{harga}     | {jumlah}         | Rp.{subtotal_1}       |\n")

        file.write(f"{spasi}{garis_kolom}\n")
        file.write(f"{spasi}|       {'Total Harga:'}                                         | Rp{total_harga_1}        |\n")
        file.write(f"{spasi}{garis_kolom}\n")

        file.write(f"{garis}\n")
        file.write(f"{spasi*6}TERIMA KASIH\n")
        file.write(f"{garis}\n")
        
    return id_transaksi_invoice

def catat_riwayat_transaksi(items, id_transaksi):
    now = datetime.now()
    waktu_transaksi = now.strftime('%Y-%m-%d %H:%M')
    id = id_transaksi
    total_harga = 0
    for item in items:
        harga, jumlah = item[1], item[2]
        harga = int(harga)
        jumlah = int(jumlah)
        subtotal = int(harga * jumlah)
        total_harga += subtotal
    Rptotal = 'Rp' + str(total_harga)
    garis_kepala = "="*64
    if os.path.exists('trx_history.txt') == False:
        with open("trx_history.txt", "a") as riwayat:
            riwayat.write(f"{garis_kepala}\n")
            riwayat.write("|                       RIWAYAT TRANSAKSI                      |".center(64) + '\n')
            riwayat.write(f"{garis_kepala}\n")
            riwayat.write("|      Waktu         |    ID Transaksi    |  Nominal Transaksi |\n")
            riwayat.write(f"{garis_kepala}\n")
            riwayat.write(f"|{waktu_transaksi:^20}|{id:^20}|{Rptotal:>20}|\n")
            riwayat.write(f"{garis_kepala}\n")
    else:
        with open("trx_history.txt", "a") as riwayat:
            riwayat.write(f"|{waktu_transaksi:^20}|{id:^20}|{Rptotal:>20}|\n")
            riwayat.write(f"{garis_kepala}\n")

print(garis)
nama_kasir = input("Masukkan nama kasir: ")

while True:
    print(garis)
    print("Pilihan:")
    print("1. Transaksi Baru")
    print("2. Cari transaksi")
    print("3. Keluar")
    print(garis)
    pilihan = input("Masukkan opsi pilihan: ")
    print(garis)
    if pilihan == "1":
        now = datetime.now()
        kasir = nama_kasir
        items = []
        total_harga = 0

        while True:
            nama_produk = input("Masukkan Nama Produk  : ")
            harga = int(input("Masukkan Harga Produk : "))
            jumlah = int(input("Masukkan Jumlah Produk: "))
            print(garis)

            items.append((nama_produk, harga, jumlah))

            lanjut = input("Tambah produk lainnya? (y/t): ").lower()
            print(garis)
            if lanjut == 'y':
                continue
            elif lanjut == 't':
                break
            else:
                print("Pilihan tidak valid")
                print(garis)
        if items:
            transaction_id = cetak_invoice(kasir, items)
            print(f"Invoice telah dicetak dengan ID transaksi: {transaction_id}")
            id = id_transaksi(kasir)
            catat_riwayat_transaksi(items, id)
        else:
            print("Transaksi kosong. Tidak ada invoice yang dicetak.")

    elif pilihan == "2":
        print(garis)
        id_dicari = input("Masukkan ID Transaksi yang ingin Anda cari: ")
        print(garis)
        nama_file = f"invoices/{id_dicari}.txt"

        try:
            with open(nama_file, "r") as file:
                isi_invoice = file.read()
            print(f"Invoice untuk ID Transaksi {id_transaksi}:\n")
            print(garis)
            print(isi_invoice)
        except FileNotFoundError:
            print(f"Invoice dengan ID Transaksi {id_transaksi} tidak ditemukan.")
            print(garis)

    elif pilihan == "3":
        print("Terima kasih! Sampai jumpa.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih opsi yang benar (1/2/3).")
