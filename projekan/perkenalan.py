# Program Perkenalan Kelompok 2

def tampilkan_kelompok():
    # Menampilkan judul di tengah
    print("\n")
    print("\n" + "KELOMPOK 2".center(140, " "))  # 60 bisa diubah sesuai lebar terminal
    print("\n" * 2)  # dua garis baru

    # Menampilkan label anggota di sisi kiri
    print("ANGGOTA KELOMPOK:")
    print("\n")  # satu garis baru

    # Menampilkan nama-nama anggota secara horizontal dengan jarak
    print("DAVA".rjust(25), "RAFFI".rjust(35), "ROZAAN".rjust(35), "AZHALIA".rjust(30))
    print("\n" * 20)  # dua garis baru

# Jalankan fungsi
tampilkan_kelompok()
