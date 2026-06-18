# 1.
print(4 == 6)
print(4 < 2)
print(4 > 8)
print(6 != 4)
print(10 <= 10)
print(9 >= 4)

# 2.
n = int(input())

if n > 100:
    print(True)
else:
    print(False)

# 3.
nilai = 85

if nilai >= 75:
    print("Lulus")

# 4.
n = int(input("Masukkan sebuah angka: "))

if n > 0:
    print("Angka positif")

if n % 2 == 0:
    print("Angka genap")

if n > 100:
    print("Angka lebih besar dari 100")

# 5.
nilai = int(input("Masukkan nilai: "))

if nilai >= 75:
    print("Lulus")
else:
    print("Tidak lulus")

# 6.
nilai = int(input("Masukkan nilai: "))

if nilai >= 85:
    print("nilai A")
elif nilai >= 70:
    print("nilai B")
elif nilai >= 60:
    print("nilai C")
else:
    print("nilai D")

# 7.
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))

if a > b:
    print("Angka pertama lebih besar dari angka kedua")
elif a < b:
    print("Angka pertama lebih kecil dari angka kedua")
else:
    print("Kedua angka sama")

# 8.
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = int(input("Masukkan angka ketiga: "))

if a >= b and a >= c:
    print("Angka terbesar adalah:", a)
elif b >= a and b >= c:
    print("Angka terbesar adalah:", b)
else:
    print("Angka terbesar adalah:", c)

# 9.
data = [4, 9, 2, 15, 7]

terbesar = max(data)
print("angka terbesar adalah:" ,terbesar)

# 10.
pendapatan = int(input("Masukkan pendapatan per tahun (rupiah): "))

if pendapatan <= 60_000_000:
    pajak = pendapatan * 0.05
elif pendapatan <= 250_000_000:
    pajak = pendapatan * 0.15
elif pendapatan <= 500_000_000:
    pajak = pendapatan * 0.25
else:
    pajak = pendapatan * 0.30

print("Total pajak yang harus dibayar:", pajak)
