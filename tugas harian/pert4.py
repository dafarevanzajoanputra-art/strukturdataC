# 1.
print("Nama :")
nama = input()

print("NIM :")
nim = input()

print("\n=== Data Mahasiswa ===")
print("Nama :", nama)
print("NIM  :", nim)

# 2.
nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")

print("\n=== Data Mahasiswa ===")
print("Nama :", nama)
print("NIM  :", nim)

# 3.
angka = input("Masukkan angka: ")
hasil = angka + 5
print(hasil)

# 4.
angka = float(input("Masukkan angka: "))
hasil = angka + 5
print(hasil)

angka = int(input("Masukkan angka: "))
hasil = angka + 8
print(hasil)

# 5.
sikuA = float(input("masukan sisi A : "))
sikuB = float(input("masukan sisi B : "))
Hypo = (sikuA**2 + sikuB**2) **.5
print ("panjang hypotenusa adalah : ", Hypo)

# 6.
sikuA = float(input("masukan sisi A : "))
sikuB = float(input("masukan sisi B : "))
print ("panjang hypotenusa adalah : ",(sikuA**2 + sikuB**2) **.5 )

# 7.
Kata1 = "Dava"
kata2 = "Revanza"
hasil = Kata1 + " " + kata2
print (hasil)

# 8.
teks = "="
hasil = teks * 10
print (hasil)

print ("=" * 10)

# 9.
sikuA = float(input("masukan sisi A : "))
sikuB = float(input("masukan sisi B : "))
Hypo = str((sikuA**2 + sikuB**2) **.5)
print ("panjang hypotenusa adalah : ", Hypo)

print (type(sikuA))
print (type(sikuB))
print (type(Hypo))

# 10.
print (type(sikuA))
print (type(sikuB))
print (type(Hypo))

# 11.
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))

penjumlahan = a + b
pengurangan = a - b
perkalian = a * b
pembagian = a / b

print("\nHasil Penjumlahan :", penjumlahan)
print("Hasil Pengurangan :", pengurangan)
print("Hasil Perkalian   :", perkalian)
print("Hasil Pembagian   :", pembagian)

print("\nSelamat kamu sudah pintar matematika")

# 12.
x = float(input("masukan nilai x : "))
y = 1.0 / (x + 1.0 /(x + 1.0 /(x - 1.0 / x)))
print ("nilai y : ", y)

# 13.
jam = int(input("Waktu mulai (jam): "))
menit = int(input("Waktu mulai (menit): "))
durasi = int(input("Durasi Acara (menit): "))

menit = menit + durasi
jam = jam + menit // 60
menit = menit % 60

print("Acara selesai pukul", jam,":",menit)