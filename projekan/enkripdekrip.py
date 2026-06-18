import numpy as np

def mod_inverse_matrix(matrix, modulus):
    """Menghitung invers matriks dalam modular (mod 26) untuk matriks 3x3"""
    # 1. Hitung determinan dan bulatkan agar menjadi integer
    det = int(np.round(np.linalg.det(matrix)))
    
    # 2. Cari modular inverse dari determinan (det * det_inv ≡ 1 mod 26)
    det_inv = -1
    for i in range(1, modulus):
        if (det * i) % modulus == 1:
            det_inv = i
            break
            
    if det_inv == -1:
        raise ValueError("Matriks tidak memiliki invers dalam mod 26! Kunci tidak valid, silakan ganti angka matriks Anda.")
        
    # 3. Hitung Adjugate matriks menggunakan sifat: adj(A) = det(A) * A^-1
    # Kita gunakan invers biasa dari numpy, lalu dikalikan dengan determinan asli
    inv_biasa = np.linalg.inv(matrix)
    adjugate = np.round(inv_biasa * det).astype(int)
    
    # 4. Invers Modular = (det_inv * adjugate) mod 26
    inverse_matrix = (det_inv * adjugate) % modulus
    return inverse_matrix.astype(int)

def encrypt(plaintext, key_matrix):
    # Membersihkan teks (kapital dan hapus spasi)
    plaintext = plaintext.upper().replace(" ", "")
    
    # Padding: jika panjang teks bukan kelipatan 3, tambahkan 'X'
    while len(plaintext) % 3 != 0:
        plaintext += 'X'
        
    ciphertext = ""
    # Proses teks per blok (ukuran 3 karakter)
    for i in range(0, len(plaintext), 3):
        p_vector = [ord(char) - 65 for char in plaintext[i:i+3]]
        c_vector = np.dot(key_matrix, p_vector) % 26
        ciphertext += ''.join([chr(val + 65) for val in c_vector])
        
    return ciphertext

def decrypt(ciphertext, key_matrix):
    # Hitung invers matriks modular 26
    key_inverse = mod_inverse_matrix(key_matrix, 26)
    
    plaintext = ""
    # Proses cipher per blok (ukuran 3 karakter)
    for i in range(0, len(ciphertext), 3):
        c_vector = [ord(char) - 65 for char in ciphertext[i:i+3]]
        p_vector = np.dot(key_inverse, c_vector) % 26
        plaintext += ''.join([chr(val + 65) for val in p_vector])
        
    return plaintext

# --- RUNNING CODE ---
# Matriks kunci 3x3 (Pastikan determinannya memiliki invers di mod 26)
# Contoh matriks ini memiliki determinan yang valid
key_matrix = np.array([
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
])

teks_asli = input("Masukan teks asli : ")

ciphertext = encrypt(teks_asli, key_matrix)
dekripsi = decrypt(ciphertext, key_matrix).rstrip('X')  # untuk menghilangkan 'X' pada akhir kalimat yang ganjil

print("\nHasil enkrip  :", ciphertext)
print("\nHasil dekrip  :", dekripsi)