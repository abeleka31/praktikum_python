class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def tampilkaninfo(self):
        return f"Nama   :{self.nama} \nNIM    :{self.nim} \nJurusan:{self.jurusan} \nIPK    :{self.ipk}"

    def hitungpredikat(self):
        if self.ipk >= 3.5:
            return "Cumlaude"
        elif 3.4 >= self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif 2.9 >= self.ipk >= 2.5:
            return "Memuaskan"
        elif 2.4 >= self.ipk >= 2.0:
            return "Cukup"
        else:
            return "kurang"
            
nama = input("Nama Mahasiswa: ")
nim = input("NIM: ")
jurusan = input("Jurusan: ")
ipk = float(input("IPK: "))

orang = Mahasiswa(nama, nim, jurusan, ipk)
info = orang.tampilkaninfo()
predikat = orang.hitungpredikat()
print("informasi Mahasiswa:")
print(info)
print("predikat yang didapat: ")
print(f"Predikat: {predikat}")
