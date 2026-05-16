# 1.
angka = [4,6,7,9,13]
print ("isi list awal: ",angka)

angka[3] = 140
print ("isi list baru: ",angka)

angka[0] = angka [4]
print ("isi list sekarang: ",angka)

# 2.
angka = [4,6,7,9,13]
print ("isi list: ",angka)

angka = [4,6,7,9,13]
print ("isi list ke-5: ",angka[4])

# 3.
angka = [4,6,7,9,13]
print("\npanjang list: ", len(angka))

# 4.
angka = [4,6,7,9,13]
print("panjang list: ", len(angka))
del angka[4]
print (angka)
# 5.
angka = [4,6,7,9,13]
print("indeks negative: ",angka[-5])
print("indeks normal  : ",angka[0])

# 6.
topi_list = [1, 2, 3, 4, 5] 

topi_list[len(topi_list)//2] = int(input("Masukkan angka: ")) 

del topi_list[-1]

print("panjang list: ",len(topi_list)) 

print(topi_list)

# 7.
angka = [1, 2, 3, 4, 5] 
print ("pangjang list: ",len(angka))
print (angka)

angka.append(7)
print ("pangjang list: ",len(angka))
print (angka)

angka.insert(3, 99)
print ("pangjang list: ",len(angka))
print (angka)

# 8.
my_list = []
for i in range(4):
    my_list.append(i+1)

print(my_list)

# 9.
my_list = []
for i in range(4):
    my_list.insert(1,i+1)

print(my_list)

# 10.
my_list = [1,2,3,5]
total = 0

for i in range(len(my_list)):
    total +=my_list[i]

print(total)
# 11.
my_list = [1,2,3,5]
total = 0

for i in my_list:
    total += i

print(total)

# 12.
my_list = [2, 9, 3, 8, 0]

length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)

# 13.
# Langkah 1: buat list kosong
exo = []
print("\nLangkah 1:", exo)


# Langkah 2: tambah anggota dengan append
exo.append("Suho")
exo.append("Kai")
exo.append("Chanyeol")
exo.append("Sehun")
print("\nLangkah 2:", exo)


# Langkah 3: tambah anggota dengan for
anggota_baru = ["DO", "Baekhyun", "Kris", "Lay", "Luhan", "Tao", "Chen"]
for member in anggota_baru:
    exo.append(member)
print("\nLangkah 3:", exo)


# Langkah 4: hapus Kris, Luhan, Tao
exo.remove("Kris")
exo.remove("Luhan")
exo.remove("Tao")
print("\nLangkah 4:", exo)


# Langkah 5: insert Xiumin di posisi ke-3 dari belakang
exo.insert(len(exo)-2, "Xiumin")
print("\nLangkah 5:", exo)


# jumlah anggota
print("\nJumlah anggota exo:", len(exo))
