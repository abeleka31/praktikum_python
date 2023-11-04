import re
def is_valid_username(username):
    pattern = r"^[A-Za-z0-9]{5,20}$" # TODO: Tambahkan pola untuk memvalidasi panjang karakter minimal 5 dan maksimal 20.
    return re.search(pattern, username)
def is_valid_email(email):
    pattern = r"^[A-Za-z0-9]{5,}@[A-Za-z0-9]+\.(com|co\.id)$" # TODO: Buatkan pola RegEx untuk validasi email.
# Sudah ada clue berupa pola untuk mencocokkan domain email.
    return re.search(pattern, email)
def is_valid_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$" # TODO: Buatkan pola RegEx untuk validasi password sesuai permintaan soal.
# Sudah ada clue berupa pola RegEx yang bisa kamu gunakan untuk menyelesaikan jawaban.
    return re.search(pattern, password)
# --------
username = input("Masukkan username: ") 
if is_valid_username(username):
    email = input("Masukkan email: ")
    if is_valid_email(email):
        password = input("Masukkan password: ")
        if is_valid_password(password):
            print("\nRegistrasi berhasil! Halo", username) # TODO: Tambahkan sapaan "Halo (username)"
        else:
            print("\nPassword yang kamu input beresiko dihack. Registrasi gagal.")
    else:
        print("\nEmail yang kamu input tidak valdi. Registrasi gagal!")
else:
    print("\nInputan username tidak valid dalam sistem. Registrasi gagal!")





