print("Pili Menu :")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

a : int(input("Masukan Pilihan Anda: "))
b : int(input("Bilangan Pertama : "))
c : int(input("Bilangann Kedua : "))

if a == "1" :
    hasil = b + c
    print(hasil)

elif a == "2":
    hasil = b - c
    print(hasil)

elif a == "3" :
    hasil = b * c
    print(hasil)

elif a == "4" : 
    hasil = b / c
    print(hasil)
