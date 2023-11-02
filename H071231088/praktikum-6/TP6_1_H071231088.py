print("Selamat datang! Untuk memulai, silakan input data anda")

def input_data():
    nama = input("Input nama: ")
    umur = input("Input umur: ")
    alamat = input("Input alamat: ")
    return {
        "Nama": nama,
        "Umur": umur,
        "Alamat": alamat
    }
def main():
    data_pengguna = input_data()
    while True:
        print("=" * 55)
        print(f"Selamat datang, {data_pengguna['Nama']}! Silakan pilih opsi:")
        print("=" * 55)
        print("1. Detail anda\n2. Ubah Nama\n3. Ubah Umur\n4. Ubah Alamat\n5. Keluar\n" + "=" * 55)
        pilihan = input("Input opsi: ")
        if pilihan == '1':
            print("=" * 55)
            print("Data Anda adalah:")
            for key, nilai in data_pengguna.items():
                print(f"{key}: {nilai}")
        elif pilihan in ('2', '3', '4'):
            if pilihan == '2':
                item = "Nama"
            elif pilihan == '3':
                item = "Umur"
            else:
                item = "Alamat"
            data_pengguna[item] = input(f"Silakan Input {item} baru: ")
            print("Data anda sukses diperbarui")
        elif pilihan == '5':
            print("=" * 55)
            print(f"Selamat Tinggal, {data_pengguna['Nama']}")
            print("=" * 55)
            print("Terima kasih! Program berakhir.")
            break
        else:
            print("Pilihan tidak valid.")
            break
main()

