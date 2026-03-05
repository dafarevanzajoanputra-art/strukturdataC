# SISTEM MANAJEMEN PERPUSTAKAAN
# Program console untuk mengelola data buku dengan fitur CRUD
# serta peminjaman dan pengembalian buku


# ===============================================
# STRUCT / CLASS BUKU
# ===============================================

class Buku:
    def __init__(self, code, judul, pengarang, genre):
        self.code = code
        self.judul = judul
        self.pengarang = pengarang
        self.genre = genre
        self.dipinjam = False


# ===============================================
# DATABASE (LIST)
# ===============================================

daftar = []


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

    code = int(input("Kode Buku      : "))
    judul = input("Judul Buku     : ")
    pengarang = input("Pengarang      : ")
    genre = input("Genre          : ")

    b = Buku(code, judul, pengarang, genre)
    daftar.append(b)

    print("\nBuku berhasil ditambahkan.")


def tampilSemua():
    bersihkan()

    if len(daftar) == 0:
        print("Tidak ada buku.")
        return

    print("DAFTAR BUKU")
    line("=", 80)

    print(f"{'Kode':<8}{'Judul':<25}{'Pengarang':<20}{'Genre':<15}{'Status':<12}")
    line("=", 80)

    for b in daftar:
        status = "Dipinjam" if b.dipinjam else "Tersedia"
        print(f"{b.code:<8}{b.judul:<25}{b.pengarang:<20}{b.genre:<15}{status:<12}")

    line("=", 80)


def cari(kode):
    for i in range(len(daftar)):
        if daftar[i].code == kode:
            return i
    return -1


def pinjam():
    bersihkan()

    kode = int(input("Masukkan kode buku yang ingin dipinjam: "))

    i = cari(kode)

    if i == -1:
        print("Buku tidak ditemukan.")
    elif daftar[i].dipinjam:
        print("Buku sudah dipinjam.")
    else:
        daftar[i].dipinjam = True
        print("Buku berhasil dipinjam.")


def kembali():
    bersihkan()

    kode = int(input("Masukkan kode buku yang dikembalikan: "))

    i = cari(kode)

    if i == -1:
        print("Buku tidak ditemukan.")
    else:
        daftar[i].dipinjam = False
        print("Buku berhasil dikembalikan.")


def update():
    bersihkan()

    kode = int(input("Masukkan kode buku yang ingin diupdate: "))

    i = cari(kode)

    if i == -1:
        print("Buku tidak ditemukan.")
        return

    print("\nData Buku")
    print("Judul    :", daftar[i].judul)
    print("Pengarang:", daftar[i].pengarang)
    print("Genre    :", daftar[i].genre)

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

    print("\nData buku diperbarui.")


def hapus():
    bersihkan()

    kode = int(input("Masukkan kode buku yang ingin dihapus: "))

    i = cari(kode)

    if i == -1:
        print("Buku tidak ditemukan.")
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