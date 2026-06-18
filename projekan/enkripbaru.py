import numpy as np

# MATRIKS KUNCI
# ============================================================
K = np.array([[6,  24,  1],
              [13, 16, 10],
              [20, 17, 15]])

# DETEMINAN MATRIKS 3x3 
# ============================================================
def determinant_mod(K, mod=26):
    """Menghitung determinan matriks 3x3 secara eksak dalam mod."""
    a, b, c = K[0, 0], K[0, 1], K[0, 2]
    d, e, f = K[1, 0], K[1, 1], K[1, 2]
    g, h, i = K[2, 0], K[2, 1], K[2, 2]
    
    # Rule of Sarrus untuk 3x3
    det = (a*e*i + b*f*g + c*d*h - c*e*g - b*d*i - a*f*h) % mod
    return det

# FUNGSI INVERS MATRIKS MODULAR
# ============================================================
def mod_inverse(a, m):
    """Mencari invers modular a terhadap m (Extended Euclidean)."""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"Invers modular tidak ada untuk a={a}, m={m}")

def matrix_mod_inverse(K, mod=26):
    """Menghitung invers matriks K dalam mod dengan kofaktor eksak."""
    det = determinant_mod(K, mod)
    det_inv = mod_inverse(det, mod)
    
    # Hitung matriks kofaktor
    cofactor = np.zeros((3, 3), dtype=int)
    
    cofactor[0, 0] = (K[1,1] * K[2,2] - K[1,2] * K[2,1]) % mod
    cofactor[0, 1] = -(K[1,0] * K[2,2] - K[1,2] * K[2,0]) % mod
    cofactor[0, 2] = (K[1,0] * K[2,1] - K[1,1] * K[2,0]) % mod
    
    cofactor[1, 0] = -(K[0,1] * K[2,2] - K[0,2] * K[2,1]) % mod
    cofactor[1, 1] = (K[0,0] * K[2,2] - K[0,2] * K[2,0]) % mod
    cofactor[1, 2] = -(K[0,0] * K[2,1] - K[0,1] * K[2,0]) % mod
    
    cofactor[2, 0] = (K[0,1] * K[1,2] - K[0,2] * K[1,1]) % mod
    cofactor[2, 1] = -(K[0,0] * K[1,2] - K[0,2] * K[1,0]) % mod
    cofactor[2, 2] = (K[0,0] * K[1,1] - K[0,1] * K[1,0]) % mod
    
    # Adjoin/adjugate = transpose dari matriks kofaktor
    adjugate = cofactor.T % mod
    
    # K^-1 = det^-1 * adjugate mod 26
    K_mod_inv = (det_inv * adjugate) % mod
    
    return K_mod_inv

# ENKRIPSI
# ============================================================
def encrypt(plaintext, K, mod=26):
    """Mengenkripsi plaintext menggunakan Hill Cipher."""
    plaintext = plaintext.upper().replace(' ', '')
    while len(plaintext) % 3 != 0:
        plaintext += 'X'
    nums = [ord(c) - ord('A') for c in plaintext]  # A=0, B=1, ..., Z=25
    ciphertext = ''
    for i in range(0, len(nums), 3):
        block = np.array(nums[i:i+3]) 
        result = K @ block % mod 
        ciphertext += ''.join(chr(int(n) + ord('A')) for n in result)
    return ciphertext

# DEKRIPSI
# ============================================================
def decrypt(ciphertext, K, mod=26):
    """Mendekripsi ciphertext menggunakan invers matriks kunci."""
    K_inv = matrix_mod_inverse(K, mod)
    nums = [ord(c) - ord('A') for c in ciphertext]  # A=0, B=1, ..., Z=25
    plaintext = ''
    for i in range(0, len(nums), 3):
        block = np.array(nums[i:i+3])  
        result = K_inv @ block % mod
        plaintext += ''.join(chr(int(n) + ord('A')) for n in result)
    return plaintext

# PROGRAM UTAMA
# ============================================================
plaintext = 'BERSIAP UNTUK APAPUN'
ciphertext = encrypt(plaintext, K)
decrypted = decrypt(ciphertext, K)

print(f"Input  (plaintext) : {plaintext}")
print(f"Output (ciphertext): {ciphertext}")
print(f"Hasil dekripsi     : {decrypted}")

plaintext = 'KRIPTOGRAFI'
ciphertext = encrypt(plaintext, K)
decrypted = decrypt(ciphertext, K)

print(f"\nInput  (plaintext) : {plaintext}")
print(f"Output (ciphertext): {ciphertext}")
print(f"Hasil dekripsi     : {decrypted}")

plaintext = 'ALJABAR'
ciphertext = encrypt(plaintext, K)
decrypted = decrypt(ciphertext, K)

print(f"\nInput  (plaintext) : {plaintext}")
print(f"Output (ciphertext): {ciphertext}")
print(f"Hasil dekripsi     : {decrypted}")