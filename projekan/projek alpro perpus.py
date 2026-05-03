# SISTEM MANAJEMEN PERPUSTAKAAN
# Program console untuk mengelola data buku dengan fitur CRUD
# serta peminjaman dan pengembalian buku

# ===============================================
# STRUCT / CLASS BUKU
# ===============================================
class Buku:
    def __init__(self, code, judul, pengarang, genre, stok=1, dipinjam=0):
        self.code = code
        self.judul = judul
        self.pengarang = pengarang
        self.genre = genre
        self.total = stok        # jumlah tersedia
        self.dipinjam = dipinjam      # jumlah yang sedang dipinjam

    def tersedia(self):
        return self.total - self.dipinjam
# ===============================================
# DATABASE (LIST)
# ===============================================
daftar = [
    Buku(101, "Laskar Pelangi", "Andrea Hirata", "Fiksi", stok=7, dipinjam=3), 
    Buku(201, "Filosofi Teras", "Henry Manampiring", "Non-Fiksi", stok=9, dipinjam=1)   
]

# ===============================================
# TOOLS
# ===============================================
def line(c, n):
    print(c * n)

def bersihkan():
    print("\033[2J\033[1;1H", end="")  

# ===============================================
# FITUR SISTEM
# ===============================================
def tambah():
    bersihkan()

    print("Tambah Buku Baru")
    line("=", 40)

    try:
        code = int(input("Kode Buku      : "))
    except ValueError:
        print("Kode harus berupa angka.")
        return

    judul = input("Judul Buku     : ")
    pengarang = input("Pengarang      : ")
    genre = input("Genre          : ")
    try:
        stok = int(input("Stok           : "))
        if stok < 0:
            print("Stok tidak boleh negatif.")
            return
    except ValueError:
        print("Stok harus berupa angka.")
        return

    b = Buku(code, judul, pengarang, genre, stok=stok)
    daftar.append(b)

    print("\nBuku berhasil ditambahkan.")

def tampilSemua():
    bersihkan()

    if len(daftar) == 0:
        print("Tidak ada buku.")
        return

    print("DAFTAR BUKU")
    line("=", 110)

    print(f"{'Kode':<8}{'Judul':<30}{'Pengarang':<25}{'Genre':<15}{'Stok':<7}{'Dipinjam':<11}{'Status':<12}")
    line("=", 110)

    for b in daftar:
        status = "Kosong" if b.tersedia() == 0 else ("Tersedia" if b.tersedia() > 0 else "Tidak tersedia")
        print(f"{b.code:<8}{b.judul:<30}{b.pengarang:<25}{b.genre:<15}{b.total:<7}{b.dipinjam:<11}{status:<12}")

    line("=", 110)

def cari(kode):
    for i in range(len(daftar)):
        if daftar[i].code == kode:
            return i
    return -1

def pinjam():
    bersihkan()

    try:
        kode = int(input("Masukkan kode buku yang ingin dipinjam: "))
    except ValueError:
        print("Kode harus berupa angka.")
        return

    i = cari(kode)

    if i == -1:
        print("Buku tidak ditemukan.")
    else:
        buku = daftar[i]
        if buku.tersedia() == 0:
            print("Stok kosong. Buku tidak dapat dipinjam.")
        else:
            buku.total -= 1
            buku.dipinjam += 1
            print("Buku berhasil dipinjam.")

def kembali():
    bersihkan()

    try:
        kode = int(input("Masukkan kode buku yang dikembalikan: "))
    except ValueError:
        print("Kode harus berupa angka.")
        return

    i = cari(kode)

    if i == -1:
        print("Buku tidak ditemukan.")
    else:
        buku = daftar[i]
        if buku.dipinjam == 0:
            print("Tidak ada salinan buku ini yang sedang dipinjam.")
        else:
            buku.dipinjam -= 1
            buku.total += 1
            print("Buku berhasil dikembalikan.")

def update():
    bersihkan()

    try:
        kode = int(input("Masukkan kode buku yang ingin diupdate: "))
    except ValueError:
        print("Kode harus berupa angka.")
        return

    i = cari(kode)

    if i == -1:
        print("Buku tidak ditemukan.")
        return

    print("\nData Buku")
    print("Judul    :", daftar[i].judul)
    print("Pengarang:", daftar[i].pengarang)
    print("Genre    :", daftar[i].genre)
    print("Stok     :", daftar[i].stok)
    print("Dipinjam :", daftar[i].dipinjam)

    line("=", 40)

    print("Kosongkan jika tidak ingin diubah.")

    judul = input("\nJudul Baru     : ")
    if judul != "":
        daftar[i].judul = judul

    pengarang = input("Pengarang Baru : ")
    if pengarang != "":
        daftar[i].pengarang = pengarang

    genre = input("Genre Baru     : ")
    if genre != "":
        daftar[i].genre = genre

    stok_input = input("Stok Baru (angka) : ")
    if stok_input != "":
        try:
            stok_baru = int(stok_input)
            if stok_baru < 0:
                print("Stok tidak boleh negatif. Perubahan stok dibatalkan.")
            else:
                # Pastikan stok minimal sama dengan jumlah yang sedang dipinjam
                if stok_baru < daftar[i].dipinjam:
                    print("Stok baru tidak boleh kurang dari jumlah yang sedang dipinjam.")
                else:
                    daftar[i].stok = stok_baru
        except ValueError:
            print("Input stok tidak valid. Perubahan stok dibatalkan.")

    print("\nData buku diperbarui.")

def hapus():
    bersihkan()

    try:
        kode = int(input("Masukkan kode buku yang ingin dihapus: "))
    except ValueError:
        print("Kode harus berupa angka.")
        return

    i = cari(kode)

    if i == -1:
        print("Buku tidak ditemukan.")
        return

    # Opsional: cek jika masih ada yang dipinjam, minta konfirmasi (sederhana: tolak hapus)
    if daftar[i].dipinjam > 0:
        print("Buku masih memiliki salinan yang dipinjam. Tidak dapat dihapus.")
        return

    daftar.pop(i)

    print("Buku berhasil dihapus.")

# ===============================================
# PROGRAM UTAMA
# ===============================================
def main():

    while True:

        bersihkan()

        print("===== MENU PERPUSTAKAAN =====")
        print("1. Tambah Buku")
        print("2. Tampilkan Semua Buku")
        print("3. Pinjam Buku")
        print("4. Kembalikan Buku")
        print("5. Update Buku")
        print("6. Hapus Buku")
        print("0. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            tambah()
        elif pilih == "2":
            tampilSemua()
        elif pilih == "3":
            pinjam()
        elif pilih == "4":
            kembali()
        elif pilih == "5":
            update()
        elif pilih == "6":
            hapus()
        elif pilih == "0":
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid.")

        input("\nTekan ENTER untuk kembali ke menu...")

if __name__ == "__main__":
    main()