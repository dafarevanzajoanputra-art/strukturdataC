# 1.
pion_putih = "<>"
baris = [pion_putih for i in range(8)]
print(baris)

# 2.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
print(matrix[0][1])
print(matrix[1][2])  

# 3.
list_3d = [
    [               # layer0
        [1, 2], 
        [3, 4],
        [5, 6]
    ],
    [               # layer1
        [7, 8],
        [9, 10],
        [11, 12]
    ]
]

print(list_3d)
print(list_3d[0][1][1])  
print(list_3d[1][2][1]) 

# 4.
def alamat (kota,desa,kodepos):
    print("\nalamat anda di ","\nkota    : ",kota,"\ndesa    : ",desa,"\nkodepos : ",kodepos)

kt = input("nama kota anda: ")
ds = input("nama desa anda: ")
kodpos = input("kodepos daerah anda: ")
alamat(kt, ds, kodpos)

# 5.
hasil = [i * 3 for i in range(1, 11) if i % 2 == 0]

print(hasil)

# 6.
matrix = []
angka = 1

for i in range(3):
    baris = []
    for j in range(3):
        baris.append(angka)
        angka += 1
    matrix.append(baris)

for baris in matrix:
    print(baris)

# 7.
data = [[2, 4], [6, 8], [10, 12]]

hasil = []

for baris in data:
    for elemen in baris:
        hasil.append(elemen)

print("Hasil: ", hasil)

# 8.
def luaspersegipanjng(a, b):
    return a * b

hasil = luaspersegipanjng(8, 5)

print("Luas persegi panjang:", hasil)