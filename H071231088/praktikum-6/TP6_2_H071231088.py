x1 = input("input array ke-1: ").split()
x2 = input("masukkan array ke-2: ").split()
set1 = set(x1)
set2 = set(x2)
duplikat = sorted(set1 & set2)
if duplikat:
    print(f"terdapat {len(duplikat)} buah duplikat yaitu ({', '.join(duplikat)}) ")
else:
    print("tidak ada duplikat ditemukan")

