# 1.
i = 1
while True:
    print("Angka:", i)
    i += 1
    
# 2.
angka = 10
while angka > 2:
    print(angka)
    angka -= 1

# 3.
ganjil = 0
genap = 0

angka = int(input("masukan angka atau ketik 0 untuk berhenti: "))
while angka != 0:
    if angka % 2 == 1:
        ganjil += 1
    else:
        genap += 1

    angka = int(input("masukan angka atau ketik 0 untuk berhenti: "))

print("Jumlah bilangan genap:", genap)
print("Jumlah bilangan ganjil:", ganjil)

# 4.
import random

print(
"""
+=============================================+
| Selamat datang di game saya, muggle!        |
| Masukkan suatu angka dan tebak              |
| angka berapa yang saya pilih                |
| untuk kamu.                                 |
| Jadi, berapa angka rahasianya?              |
+=============================================+
""")

secret_number = random.randint(1, 10)  # angka acak dari 1 sampai 10

while True:
    angka = int(input("Tebak angka (1-10): "))

    if angka == secret_number:
        print("Selamat, Muggle! kamu bebas sekarang!")
        break
    else:
        print("hahaha ! kamu nyangkut deh di Loop saya")

# 5.
# Contoh A: range(stop)
print("Contoh A: range(10)")
for a in range(10):
    print("nilai a saat ini adalah", a)

# Contoh B: range(start, stop)
print("\nContoh B: range(2, 8)")
for b in range(2, 8):
    print("nilai b saat ini adalah", b)

# Contoh C: range(start, stop, step)
print("\nContoh C: range(2, 8, 3)")
for c in range(2, 8, 3):
    print("nilai c saat ini adalah", c)

# Contoh D: Range Kosong (Start == Stop)
print("\nContoh D: range(1, 1)")
for d in range(1, 1):
    print("nilai d saat ini adalah", d)
print("(Tidak ada output karena start sama dengan stop)")

# Contoh E: Range Kosong (Start > Stop tanpa negatif step)
print("\nContoh E: range(2, 1)")
for e in range(2, 1):
    print("nilai e saat ini adalah", e)
print("(Tidak ada output karena tidak bisa melompat maju dari 2 ke 1)")

# 6.
power = 1
for expo in range(11):
    print("2 pangkat", expo, "adalah", power)
    power *= 2

# 7.
print ("continue")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print ("\nbreak")
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# 8.
import random

print(
"""
+=============================================+
| Selamat datang di game saya, muggle!        |
| Masukkan suatu angka dan tebak              |
| angka berapa yang saya pilih                |
| untuk kamu.                                 |
| Jadi, berapa angka rahasianya?              |
+=============================================+
""")

secret_number = random.randint(1, 10)  # angka acak dari 1 sampai 10

while True:
    angka = int(input("Tebak angka (1-10): "))

    if angka == secret_number:
        print("Selamat, Muggle! kamu bebas sekarang!")
        break
    else:
        print("hahaha ! kamu nyangkut deh di Loop saya")

# 9.
user_word = input("Masukkan suatu kata: ")

user_word = user_word.upper() #membuat huruf agar kapital

for kata in user_word:
   
    if kata == "A" or kata == "I" or kata == "U" or kata == "E" or kata == "O":
        continue
                       
    print(kata)

# 10.
hitung = 3

while hitung > 0:
    print("Hitung mundur:", hitung)
    hitung -= 1  # Mengurangi hitung 
else:
    print("Wush! Roket meluncur!")

# 11.
for i in range(1, 6):
    print("Hitungan ke ", i)
else:
    print("Petak Umpet Dimulai!!!")

# 12.
nilai = int(input("Masukan Nilai: "))
kehadiran = int(input("Masukan Kehadiran: "))

if nilai > 75 and kehadiran > 80:
    print("Lulus")
else:
    print("Tidak Lulus")

# 13.
a = 12  # Biner: 1100
b = 10  # Biner: 1010

print ("Biner A = 1100")
print ("Biner B = 1010")
print ("=" * 30)

# a. Bitwise AND (&)
print(f"A & B  = {a & b}  (Hanya 1 jika keduanya 1 dan sisanya 0)")

# b. Bitwise OR (|)
print(f"A | B  = {a | b} (Hanya 0 jika keduanya 0 dan sisanya 1)")

# c. Bitwise XOR (^)
print(f"A ^ B  = {a ^ b}  (Hanya 1 jika bit berbeda. jika sama 0)")

# d. Bitwise NOT (~)
print(f"~A     = {~a} (Rumus: -(x + 1))")

# 14.
a = 12  
b = 10  

print ("Biner A = 1100")
print ("Biner B = 1010")
print ("=" * 30)

# a. Bitwise Left Shift (<<)
print(f"A << 1 = {a << 2} (Geser kiri 2x = dikali 4)")

# b. Bitwise Right Shift (>>)
print(f"A >> 1 = {a >> 2}  (Geser kanan 2x = dibagi 4)")

# 15.
x = 4  
y = 1 

print ("Biner x = 0100")
print ("Biner y = 0001")

a = x & y  # 0100 & 0001 = 0000 (1 jika keduanya 1 dan sisanya 0) (0)
b = x | y  # 0100 | 0001 = 0101 (0 jika keduanya 0 sisanya 1) (5)
c = ~x     # -(4 + 1) = -5 (dari rumus -(x+1)) (-5)
d = x ^ 5  # 0100 ^ 0101 = 0001  (1 jika bit berbeda sisanya 0) (1)
e = x >> 2 # 0100 menjadi 0001 (geser kanan 2x) (0100 > 0010 > 0001) (1)
