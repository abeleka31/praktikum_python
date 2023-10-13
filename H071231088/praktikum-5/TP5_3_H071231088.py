kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

def anagram(kata1, kata2):
    kata1, kata2 = kata1.replace(" ", "").lower(), kata2.replace(" ", "").lower()
    if len(kata1) != len(kata2):
        return False
    
    set_kata1 = set(kata1)
    set_kata2 = set(kata2)

    return set_kata1 == set_kata2

if anagram(kata1, kata2):
    print("true")
else:
    print("false")
