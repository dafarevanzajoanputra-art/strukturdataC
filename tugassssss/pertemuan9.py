# 1.
my_list = [3, 1, 9, 7, 5]
swapped = True # inisialisasi awal untuk memasuki loop

while swapped:
    swapped = False # untuk mengindikasikan tidak ada pertukaran elemen
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)

# 2.
my_list = []
swapped = True
angka = int(input("Masukkan panjang elemen list yang ingin diurutkan : "))

for i in range(angka):
    val = float(input("Masukkan elemen list : "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\n Terurut : ")
print(my_list)

# 3.
list_aku = [11, 19, 27, 15, 13]
list_aku.sort()
print(list_aku)

# 4.
list = [10, 7, 9, 6, 8]
list.reverse()
print(list)

# 5.
list_1 = [5]
list_2 = list_1
list_1[0] = 10
print(list_2)

# 6.
list_saya = [9, 7, 5, 3, 1]
list_baru = list_saya[1:3]
print(list_baru)

# 7.
lemari = [10, 6, 7, 5, 2]
new_lemari = lemari[1:-1]
print(new_lemari)

# 8.
lemari = [10, 6, 7, 5, 2]
new_lemari = lemari[-1:1]
print(new_lemari)

# 9.
lemari = [10, 6, 7, 5, 2]
new_lemari = lemari[:2]
print(new_lemari)

# 10.
lemari = [10, 6, 7, 5, 2]
new_lemari = lemari[-4:]
print(new_lemari)

# 11.
lemari = [10, 6, 7, 5, 2]
new_lemari = lemari[:]
print(new_lemari)

# 12.
lemari = [10, 6, 7, 5, 2]
del lemari [1:-1]
print(lemari)

# 13.
lemari = [10, 6, 7, 5, 2]
del lemari [:]
print(lemari)

# 14.
lemari = [10, 6, 7, 5, 2]
del lemari 
print(lemari)

# 15.
lemari = [10, 6, 7, 5, 2]
print(5 in lemari)

# 16.
lemari = [10, 6, 7, 5, 2]
print(5 not in lemari)

# 17.
lemari = [10, 6, 7, 5, 2, 4, 22, 13, 17]
largest = lemari[0]
for i in range(1, len(lemari)):
    if lemari[i] > largest:
        largest = lemari[i]

print(largest)

# 18.
lemari = [10, 6, 7, 5, 2, 4, 22, 13, 17]
largest = lemari[0]

for i in lemari:
    if i > largest:
        largest = i

print(largest)

# 19.
lemari = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(lemari)):
    found = lemari[i] == to_find
    if found:
        break

if found:
    print("element ditemukan pada indeks ke- ", i)
else:
    print("element tidak ada pada list")

# 20.
tebakan = [3, 7, 11, 42, 34, 49]
hasil = [5, 9, 11, 42, 3, 49]

benar = 0

for angka in tebakan:
    if angka in hasil:
        benar += 1

print("Jumlah tebakan benar:", benar)

# 21.
lemari = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

unik = []

for angka in lemari:
    if angka not in unik:
        unik.append(angka)

print("List tanpa duplikat:", unik)