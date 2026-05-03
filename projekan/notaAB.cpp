#include <iostream>
#include <iomanip>
#include <cstdlib>
using namespace std;

// Fungsi center
void centerText(string text, int width) {
    int space = (width - text.length()) / 2;
    for (int i = 0; i < space; i++) cout << " ";
    cout << text << endl;
}

int main() {
    string barang[] = {"Armor", "Helm", "Senjata", "Peluru", "Termal"};
    string tier[5];
    int qty[5], harga[5];
    int totalQty = 0;
    int totalHarga = 0;
    int lebar = 50;
    char pilih;

    cout << "Masukkan data (ENTER = lanjut, N = edit):\n";

    for (int i = 0; i < 5; i++) {
        while (true) {
            cout << "\n" << barang[i] << endl;

            // Input Tier
            cout << "Tier  : ";
            cin >> tier[i];

            // Input Qty
            do {
                cout << "Qty   : ";
                cin >> qty[i];
            } while (qty[i] < 0);

            // Input Harga
            do {
                cout << "Harga : ";
                cin >> harga[i];
            } while (harga[i] < 0);

            cin.ignore();

            cout << "Tekan ENTER untuk lanjut / N untuk edit: ";
            pilih = cin.get();

            if (pilih == 'n' || pilih == 'N') {
                cout << "Input diulang...\n";
                continue;
            }
            break;
        }
    }

    system("clear");

    // Judul
    centerText("===== Nota Pembelian =====\n", lebar);

    // Header tabel
    cout << left << setw(26) << "Perlengkapan"
         << setw(6)  << "Tier"
         << setw(8)  << "Qty"
         << setw(10) << "Harga" << endl;

    cout << "-------------------------------------------------" << endl;

    // Isi tabel
    for (int i = 0; i < 5; i++) {
        cout << left << setw(26) << barang[i]
             << setw(6)  << tier[i]
             << setw(8)  << qty[i]
             << setw(10) << harga[i] << endl;

        totalQty += qty[i];
        totalHarga += harga[i];
    }

    cout << "-------------------------------------------------" << endl;

    // Total
    cout << left << setw(26) << "TOTAL"
         << setw(6)  << "-"
         << setw(8)  << totalQty
         << setw(10) << totalHarga << endl;

    cout << "-------------------------------------------------" << endl;

    // Footer
    centerText("Pembayaran bisa melalui DANA", lebar);
    centerText("No: 083892130352", lebar);

    cout << endl;
    centerText("NOTE:", lebar);
    centerText("Perlengkapan pinjaman yang dibawa pulang", lebar);
    centerText("bisa dipakai kembali sampai hilang", lebar);

    return 0;
}