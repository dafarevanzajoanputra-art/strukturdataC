import random
import os

def clear_screen():
    # Deteksi OS untuk clear terminal
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # Linux/Mac
        os.system("clear")

def turnamen():
    clear_screen()  # Bersihkan layar saat game baru dimulai

    # Input jumlah peserta
    n = int(input("Masukkan jumlah peserta: "))
    peserta = []
    for i in range(n):
        nama = input(f"Nama peserta {i+1}: ")
        peserta.append(nama)

    # Acak urutan peserta
    random.shuffle(peserta)

    ronde = 1
    while len(peserta) > 1:
        print(f"\n=== Ronde {ronde} ===")
        pemenang = []
        for i in range(0, len(peserta), 2):
            if i+1 < len(peserta):
                print(f"{peserta[i]} vs {peserta[i+1]}")
                winner = input("Masukkan nama pemenang: ")
                while winner not in [peserta[i], peserta[i+1]]:
                    winner = input("Nama tidak valid, masukkan lagi: ")
                pemenang.append(winner)
            else:
                # bye otomatis lolos
                print(f"{peserta[i]} lolos otomatis")
                pemenang.append(peserta[i])
        peserta = pemenang
        ronde += 1

    print(f"\nJuara Turnamen: {peserta[0]} 🏆")

# Jalankan
turnamen()
