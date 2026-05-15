import random

def turnamen():
    peserta = ["dava", "nafis", "alfan", "rozaan", "rasya", "maman"]

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
                print(f"{peserta[i]} lolos otomatis")
                pemenang.append(peserta[i])
        peserta = pemenang
        ronde += 1

    print(f"\nJuara Turnamen Biliard: {peserta[0]}")

turnamen()