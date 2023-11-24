import re
garis = "="*60
class DataPengguna:
    def __init__(self):
        self.data = {'Nama': '', 'Email': '', 'Password': ''}

    def tampilkan_detail(self):
        if not self.data['Nama']:
            print("Data saat ini kosong" )
        else:
            print("Detail Data adalah")
            for key, value in self.data.items():
                print(f"{key}: {value}")

    def ubah_nama(self):
        if not self.data['Nama']:
            print("Data saat ini kosong")
        else:
            new_name = input("Masukkan nama baru: ")
            self.data['Nama'] = new_name
            print("Nama berhasil diubah")

    def validasi_email(self, email):
        return re.match(r"[a-z0-9._%+-]+@student.unhas.ac.id$", email)

    def validasi_password(self, password):
        return 8 <= len(password) <= 20 and any(x.isupper() for x in password) and any(x.islower() for x in password) and any(x.isdigit() for x in password)

    def buat_data_baru(self):
        nama = input("Masukkan Nama: ")

        while True:
            email = input("Masukkan Email: ")
            if self.validasi_email(email):
                break
            else:
                print("Email yang Anda Masukkan Salah")

        while True:
            password = input("Masukkan Password: ")
            if self.validasi_password(password):
                break
            else:
                print("Password yang Anda Masukkan terlalu lemah. Gunakan minimal 1 huruf kapital, huruf kecil, dan angka.")

        self.data = {'Nama': nama, 'Email': email, 'Password': password}
        print("Data berhasil dibuat")

    def simpan_data_ke_file(self):
        if not any(self.data.values()):
            print(garis + "\nData saat ini kosong. Tidak ada yang disimpan.\n" + garis)
            return

        nama_file = input("Masukkan nama file tanpa format '.txt' (atau tekan Enter untuk kembali): ")
        if not nama_file:
            print(garis + "\nData saat ini kosong. Tidak ada yang disimpan.\n" + garis)
            return

        nama_file += '.txt'

        with open(nama_file, 'a') as file:
            if not file.tell():  # Cek apakah file masih kosong
                file.write("+" + "=" * 55)
                file.write("\n| Data yang Tersimpan")
                file.write("\n+" + "=" * 55)

            file.write(f"\n| Nama      : {self.data['Nama']}\n")
            file.write(f"| Email     : {self.data['Email']}\n")
            file.write(f"| Password  : {self.data['Password']}")
            file.write("\n+" + "=" * 55)
            self.data = {'Nama': '', 'Email': '', 'Password': ''}

        print("Berhasil menyimpan data pada file")

def hitung_jumlah_data(nama_file):
    try:
        with open(f"{nama_file}.txt", 'r') as file:
            hitung_data = sum(1 for baris in file)
            hitung_data -= 3
            hitung_data //= 4 
            print(f"Jumlah Data pada File: {hitung_data} Data")
    except FileNotFoundError:
        print(f"Tidak Terdapat File dengan Nama {nama_file}.txt")
        print("Jumlah Data pada File: 0 Data")


def main():
    data_pengguna = DataPengguna()
    while True:
        print(garis + "\nSelamat datang Silahkan pilih opsi menu anda:")
        print("1. Tampilkan Detail Anda")
        print("2. Ubah Nama")
        print("3. Jumlah Data pada File")
        print("4. Simpan Data pada File")
        print("5. Buat Data Baru")
        print("6. Keluar\n" + garis)

        pilihan = input("masukkan pilihan anda: ")
        print(garis)
        match pilihan:
            case '1':
                data_pengguna.tampilkan_detail()
            case '2':
                data_pengguna.ubah_nama()
            case '3':
                nama_file = input("Masukkan nama file: ")
                hitung_jumlah_data(nama_file)
            case '4':
                data_pengguna.simpan_data_ke_file()
            case '5':
                data_pengguna.buat_data_baru()
            case '6':
                print("Sampai Jumpa Lagi")
                break
            case _:
                print("Pilihan tidak valid. Silakan pilih menu (1-6)")

if __name__ == "__main__":
    main()
