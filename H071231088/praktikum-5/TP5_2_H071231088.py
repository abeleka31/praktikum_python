kata = input("masukkan kata: ")
kata = kata.replace(" ", "")
def ATH(karakter):
    panjang = len(karakter)
    if panjang < 3:
        return "invalid."

    awal = karakter[0]
    akhir = karakter[-1]

    kata_tengah = panjang // 2
    if panjang % 2 == 0:
        tengah = karakter[kata_tengah - 1:kata_tengah + 1]
    else:
        tengah = karakter[kata_tengah]

    hasil = f"{awal}{tengah}{akhir}"

    return hasil

hasil_akhir = ATH(kata)
print(hasil_akhir)
