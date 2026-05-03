daftar = []

def line(c, n):
    print(c * n)

def bersihkan():
    print("\033[2J\033[1;1H", end="")


def tambah():
    """Menambahkan buku baru dengan jumlah stok"""
    bersihkan()
    print("Tambah Buku Baru")
    line('=', 40)
    
    try:
        kode = int(input("Kode Buku      : "))
        judul = input("Judul Buku     : ")
        pengarang = input("Pengarang      : ")
        genre = input("Genre          : ")
        stok = int(input("Jumlah Stok    : ")) # Input stok baru
        
        buku_baru = {
            "code": kode,
            "judul": judul,
            "pengarang": pengarang,
            "genre": genre,
            "stok": stok,          # Total stok yang dimiliki
            "dipinjam_count": 0    # Jumlah yang sedang keluar
        }
        
        daftar.append(buku_baru)
        print("\nBuku berhasil ditambahkan.")
    except ValueError:
        print("\nInput angka tidak valid!")

def tampil_semua():
    """Menampilkan daftar buku dengan info stok sisa"""
    bersihkan()
    
    if not daftar:
        print("Tidak ada buku.")
        return

    print("DAFTAR BUKU")
    line('=', 95)
    
    # Menyesuaikan lebar kolom untuk kolom stok
    print(f"{'Kode':<8}{'Judul':<25}{'Pengarang':<20}{'Genre':<15}{'Total':<10}{'Tersedia':<10}")
    line('=', 95)

    for b in daftar:
        # Stok tersedia = Total stok - jumlah yang dipinjam
        tersedia = b['stok'] - b['dipinjam_count']
        print(f"{b['code']:<8}{b['judul']:<25}{b['pengarang']:<20}{b['genre']:<15}{b['stok']:<10}{tersedia:<10}")
    
    line('=', 95)

def cari(kode):
    for i in range(len(daftar)):
        if daftar[i]['code'] == kode:
            return i
    return -1

def pinjam():
    """Peminjaman akan mengurangi stok yang tersedia"""
    bersihkan()
    try:
        kode = int(input("Masukkan kode buku yang ingin dipinjam: "))
        i = cari(kode)
        
        if i == -1:
            print("Buku tidak ditemukan.")
        else:
            # Cek apakah masih ada stok sisa
            if daftar[i]['dipinjam_count'] < daftar[i]['stok']:
                daftar[i]['dipinjam_count'] += 1
                print(f"Berhasil meminjam '{daftar[i]['judul']}'.")
                print(f"Sisa stok: {daftar[i]['stok'] - daftar[i]['dipinjam_count']}")
            else:
                print("Maaf, stok buku ini sedang kosong (semua sedang dipinjam).")
    except ValueError:
        print("Input tidak valid.")

def kembali():
    """Pengembalian akan menambah stok yang tersedia"""
    bersihkan()
    try:
        kode = int(input("Masukkan kode buku yang dikembalikan: "))
        i = cari(kode)
        
        if i == -1:
            print("Buku tidak ditemukan.")
        elif daftar[i]['dipinjam_count'] <= 0:
            print("Kesalahan: Tidak ada record peminjaman untuk buku ini.")
        else:
            daftar[i]['dipinjam_count'] -= 1
            print(f"Buku '{daftar[i]['judul']}' telah dikembalikan.")
    except ValueError:
        print("Input tidak valid.")

def update():
    """Update info buku termasuk stok total"""
    bersihkan()
    try:
        kode = int(input("Masukkan kode buku yang ingin diupdate: "))
        i = cari(kode)
        
        if i == -1:
            print("Buku tidak ditemukan.")
            return

        print(f"\nData Buku Saat Ini (Kosongkan jika tidak diubah):")
        line('-', 40)
        
        s = input(f"Judul [{daftar[i]['judul']}]: ")
        if s: daftar[i]['judul'] = s
            
        s = input(f"Pengarang [{daftar[i]['pengarang']}]: ")
        if s: daftar[i]['pengarang'] = s
            
        s = input(f"Stok Total [{daftar[i]['stok']}]: ")
        if s: daftar[i]['stok'] = int(s)

        print("\nData buku diperbarui.")
    except ValueError:
        print("Input angka tidak valid.")

def hapus():
    bersihkan()
    try:
        kode = int(input("Masukkan kode buku yang ingin dihapus: "))
        i = cari(kode)
        if i != -1:
            daftar.pop(i)
            print("Buku berhasil dihapus.")
        else:
            print("Buku tidak ditemukan.")
    except ValueError:
        print("Input tidak valid.")

# ===============================================
# MAIN LOOP
# ===============================================

def main():
    while True:
        bersihkan()
        print("===== SISTEM PERPUSTAKAAN (DENGAN STOK) =====")
        print("1. Tambah Buku & Stok")
        print("2. Tampilkan Katalog")
        print("3. Pinjam Buku")
        print("4. Kembalikan Buku")
        print("5. Update Data/Stok")
        print("6. Hapus Buku")
        print("0. Keluar")
        
        pilih = input("Pilih menu: ")
        
        if pilih == '1': tambah()
        elif pilih == '2': tampil_semua()
        elif pilih == '3': pinjam()
        elif pilih == '4': kembali()
        elif pilih == '5': update()
        elif pilih == '6': hapus()
        elif pilih == '0': break
        
        input("\nTekan ENTER untuk kembali...")

if __name__ == "__main__":
    main()