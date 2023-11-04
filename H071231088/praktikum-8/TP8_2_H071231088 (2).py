import re

def tentukan_ip(jumlah_input):
    hasil = []
    
    for _ in range(jumlah_input):
        inputan = input("Masukkan alamat IP: ").strip()

        pattern_1 = r'^(\d{1,3}\.){3}\d{1,3}$'
        pattern_2 = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
        ipv4 = re.match(pattern_1, inputan)
        ipv6 = re.match(pattern_2, inputan)
        if ipv4 and all(0 <= int(segment) <= 255 for segment in ipv4.group(0).split('.')):
            hasil.append("IPv4")
        elif ipv6:
            hasil.append("IPv6")
        else:
            hasil.append("Bukan IP Address")

    return hasil

jumlah_input = int(input("Masukkan jumlah alamat IP yang akan diperiksa: "))
hasil = tentukan_ip(jumlah_input)

for i in hasil:
    print(i)
