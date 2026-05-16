import numpy as np

# Fungsi untuk mengubah huruf menjadi angka (A=0, B=1, ..., Z=25)
def huruf_ke_angka(text):
    return [ord(c.upper()) - ord('A') for c in text if c.isalpha()]

# Fungsi untuk mengubah angka kembali menjadi huruf
def angka_ke_huruf(angka):
    return ''.join([chr(n % 26 + ord('A')) for n in angka])

# Fungsi enkripsi Hill Cipher
def hill_encrypt(plaintext, key_matrix):
    n = key_matrix.shape[0]
    angka = huruf_ke_angka(plaintext)
    
    # Padding jika panjang tidak habis dibagi n
    while len(angka) % n != 0:
        angka  .append(ord('X') - ord('A'))  # tambahkan 'X'
    
    ciphertext = []
    for i in range(0, len(angka), n):
        block = np.array(angka[i:i+n])
        enkripsi_block = key_matrix.dot(block) % 26
        ciphertext.extend(enkripsi_block)
    
    return angka_ke_huruf(ciphertext)

# Fungsi dekripsi Hill Cipher
def hill_decrypt(ciphertext, key_matrix):
    n = key_matrix.shape[0]
    angka = huruf_ke_angka(ciphertext)
    
    # Hitung invers matriks modulo 26
    det = int(round(np.linalg.det(key_matrix)))
    det_inv = pow(det % 26, -1, 26)  # invers determinan mod 26
    
    adjugate = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
    inv_matrix = (det_inv * adjugate) % 26
    
    plaintext = []
    for i in range(0, len(angka), n):
        block = np.array(angka[i:i+n])
        dekripsi_block = inv_matrix.dot(block) % 26
        plaintext.extend(dekripsi_block)
    
    return angka_ke_huruf(plaintext)

# Contoh penggunaan
key_matrix = np.array([[3, 3], [2, 5]])  # matriks kunci 2x2
teks_asli = "jerman mengirmkan tank panzer"  

ciphertext = hill_encrypt(teks_asli, key_matrix)
dekripsi = hill_decrypt(ciphertext, key_matrix).rstrip('X') # untuk menghilangkan x pada akhir kalimat yang ganjil


print("kalimat asli  :", teks_asli )
print("hasil enkrip  :", ciphertext)
print("hasil deskrip :", dekripsi)
