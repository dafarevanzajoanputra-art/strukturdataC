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