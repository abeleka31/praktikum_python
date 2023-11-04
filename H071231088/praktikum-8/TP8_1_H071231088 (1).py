import re
inputan = input("Masukkan inputan: ")
if len(inputan) == 45 and re.findall(r'[a-zA-Z02468]', inputan[:40]) and re.findall(r'[13579\s]', inputan[40:]):
    print("True")
else:
    print("False")
