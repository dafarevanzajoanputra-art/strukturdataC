import os

# Fungsi center
def center_text(text, width):
    space = (width - len(text)) // 2
    print(" " * space + text)

def main():
    barang = ["Armor", "Helm", "Senjata", "Peluru", "Termal"]
    tier = [""] * 5
    qty = [0] * 5
    harga = [0] * 5

    total_qty = 0
    total_harga = 0
    lebar = 50

    print("Masukkan data (ENTER = lanjut, N = edit):")

    for i in range(5):
        while True:
            print(f"\n{barang[i]}")

            # Input Tier
            tier[i] = input("Tier  : ")

            # Input Qty
            while True:
                try:
                    qty[i] = int(input("Qty   : "))
                    if qty[i] >= 0:
                        break
                except:
                    pass

            # Input Harga
            while True:
                try:
                    harga[i] = int(input("Harga : "))
                    if harga[i] >= 0:
                        break
                except:
                    pass

            pilih = input("Tekan ENTER untuk lanjut / N untuk edit: ")

            if pilih.lower() == 'n':
                print("Input diulang...")
                continue
            break

    # Clear screen (opsional)
    os.system('cls' if os.name == 'nt' else 'clear')

    # Judul
    center_text("===== Nota Pembelian =====", lebar)
    print()

    # Header tabel
    print(f"{'Perlengkapan':<26}{'Tier':<6}{'Qty':<8}{'Harga':<10}")
    print("-" * 49)

    # Isi tabel
    for i in range(5):
        print(f"{barang[i]:<26}{tier[i]:<6}{qty[i]:<8}{harga[i]:<10}")
        total_qty += qty[i]
        total_harga += harga[i]

    print("-" * 49)

    # Total
    print(f"{'TOTAL':<26}{'-':<6}{total_qty:<8}{total_harga:<10}")
    print("-" * 49)

    # Footer
    center_text("Pembayaran bisa melalui DANA", lebar)
    center_text("No: 083892130352", lebar)

    print()
    center_text("NOTE:", lebar)
    center_text("Perlengkapan pinjaman yang dibawa pulang", lebar)
    center_text("bisa dipakai kembali sampai hilang", lebar)

if __name__ == "__main__":
    main()