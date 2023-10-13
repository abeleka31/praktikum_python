#masukkan inputan
s1 = input("Masukkan s1: ")
s2 = input("Masukkan s2: ")

def kata(s1, s2):
    i, j = 0, len(s2) - 1 
    s3 = "" 

    while i < len(s1) or j >= 0:
        if i < len(s1) and s1[i] != ' ':
            s3 += s1[i]
        if j >= 0 and s2[j] != ' ':
            s3 += s2[j]
        i += 1
        j -= 1

    return s3

s3 = kata(s1, s2)
print(s3)

















