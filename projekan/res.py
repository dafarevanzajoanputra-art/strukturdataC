import os

inventory = {}
riwayat = []

def bersihkan():
    os.system('cls' if os.name == 'nt' else 'clear')


def dashboard():
    if not inventory:
        print("\nGudang masih kosong.")
        input("\nTekan Enter untuk kembali...")
        bersihkan()
        return

    total_stok = 0
    total_nilai = 0
    stok_rendah = 0

    print("\n=== DATA BARANG ===")
    for kode, data in inventory.items():
        nilai = data['stok'] * data['harga']
        print(f"Kode: {kode} | Nama: {data['nama']} | Stok: {data['stok']} | Harga Jual: Rp {data['harga']:,} | Nilai: Rp {nilai:,} | Lokasi: {data['lokasi']}")
        total_stok += data['stok']
        total_nilai += nilai
        if data['stok'] < 10:
            stok_rendah += 1

    print(f"\nTotal Jenis Barang    : {len(inventory)}")
    print(f"Total Seluruh Stok    : {total_stok} unit")
    print(f"Total Nilai Inventaris: Rp {total_nilai:,}")
    print(f"Stok Rendah (<10)     : {stok_rendah} jenis")
    input("\nTekan Enter untuk kembali...")
    bersihkan()


def tambah_barang():
    kode = input("\nKode Barang: ").upper()

    if kode in inventory:
        print("Kode sudah dipakai!")
        input("\nTekan Enter untuk kembali...")
        bersihkan()
        return

    nama = input("Nama Barang: ")
    lokasi = input("Lokasi: ")

    try:
        stok = int(input("Stok Awal: "))
        harga = int(input("Harga Jual Satuan (Rp): "))
    except:
        print("Stok dan harga harus angka!")
        input("\nTekan Enter untuk kembali...")
        bersihkan()
        return

    inventory[kode] = {
        "nama": nama,
        "stok": stok,
        "lokasi": lokasi,
        "harga": harga
    }

    print("Barang berhasil ditambahkan!")
    input("\nTekan Enter untuk kembali...")
    bersihkan()


def transaksi():
    kode = input("\nMasukkan kode barang: ").upper()

    if kode not in inventory:
        print("Barang tidak ditemukan!")
        input("\nTekan Enter untuk kembali...")
        bersihkan()
        return

    data = inventory[kode]
    print(f"Nama: {data['nama']} | Stok sekarang: {data['stok']} | Harga Jual: Rp {data['harga']:,}")

    print("1. Masuk (+)")
    print("2. Keluar (-)")

    pilihan = input("Pilih: ")

    try:
        jumlah = int(input("Jumlah: "))
    except:
        print("Jumlah harus angka!")
        input("\nTekan Enter untuk kembali...")
        bersihkan()
        return

    if pilihan == "1":
        try:
            harga_beli = int(input("Harga Beli Satuan (Rp): "))
        except:
            print("Harga harus angka!")
            input("\nTekan Enter untuk kembali...")
            bersihkan()
            return

        inventory[kode]['stok'] += jumlah
        total_beli = harga_beli * jumlah

        riwayat.append({
            "kode": kode,
            "nama": data['nama'],
            "tipe": "MASUK",
            "jumlah": jumlah,
            "harga_beli": harga_beli,
            "total_beli": total_beli
        })

        print(f"Stok ditambah! Total Beli: Rp {total_beli:,}")

    elif pilihan == "2":
        if data['stok'] >= jumlah:
            inventory[kode]['stok'] -= jumlah
            total_jual = data['harga'] * jumlah
            riwayat.append({
                "kode": kode,
                "nama": data['nama'],
                "tipe": "KELUAR",
                "jumlah": jumlah,
                "harga_jual": data['harga'],
                "total_harga": total_jual
            })
            print(f"Stok dikurangi! Total Jual: Rp {total_jual:,}")
        else:
            print("Stok tidak cukup!")
    else:
        print("Pilihan tidak valid!")

    input("\nTekan Enter untuk kembali...")
    bersihkan()


def lihat_riwayat():
    if not riwayat:
        print("\nBelum ada transaksi.")
        input("\nTekan Enter untuk kembali...")
        bersihkan()
        return

    total_pemasukan = 0
    total_pengeluaran = 0

    print("\n=== RIWAYAT TRANSAKSI ===")
    for r in riwayat:
        if r['tipe'] == "MASUK":
            total_pengeluaran += r['total_beli']
            print(f"{r['kode']} - {r['nama']} | MASUK {r['jumlah']} | "
                  f"Harga Beli: Rp {r['harga_beli']:,} | Total: Rp {r['total_beli']:,}")
        else:
            total_pemasukan += r['total_harga']
            print(f"{r['kode']} - {r['nama']} | KELUAR {r['jumlah']} | "
                  f"Harga Jual: Rp {r['harga_jual']:,} | Total: Rp {r['total_harga']:,}")

    print(f"\nTotal Pemasukan  : Rp {total_pemasukan:,}")
    print(f"Total Pengeluaran: Rp {total_pengeluaran:,}")
    input("\nTekan Enter untuk kembali...")
    bersihkan()


def hapus_barang():
    kode = input("\nMasukkan kode barang yang mau dihapus: ").upper()

    if kode in inventory:
        nama = inventory[kode]['nama']
        del inventory[kode]
        print(f"{nama} berhasil dihapus.")
    else:
        print("Barang tidak ditemukan!")

    input("\nTekan Enter untuk kembali...")
    bersihkan()


# --- MAIN PROGRAM ---
while True:
    print("\n=== WAREHOUSE SYSTEM ===")
    print("1. Dashboard")
    print("2. Tambah Barang")
    print("3. Transaksi")
    print("4. Hapus Barang")
    print("5. Riwayat Transaksi")
    print("0. Keluar")

    menu = input("Pilih menu: ")

    if menu == "1":
        dashboard()
    elif menu == "2":
        tambah_barang()
    elif menu == "3":
        transaksi()
    elif menu == "4":
        hapus_barang()
    elif menu == "5":
        lihat_riwayat()
    elif menu == "0":
        print("Keluar program...")
        break
    else:
        print("Menu tidak valid!")