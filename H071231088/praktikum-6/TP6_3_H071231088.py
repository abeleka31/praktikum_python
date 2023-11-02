
angka = input("Masukkan beberapa angka dengan spasi: ").split(" ")
genap, ganjil, lima = [], [], []
for item in angka:
    i = int(item)

    if i % 2 == 0 and i not in genap:
        genap.append(i)
    if i % 2 != 0 and i not in ganjil:
        ganjil.append(i)
    if i % 5 == 0 and i not in lima:
        lima.append(i)

x1 = list(genap)
genap = sorted(x1)
x2 = list(ganjil)
ganjil = sorted(x2)
x3 = list(lima)
lima = sorted(x3)

print(f"Angka genap: {genap}\nAngka ganjil: {ganjil}\nAngka yang habis dibagi 5: {lima}")






