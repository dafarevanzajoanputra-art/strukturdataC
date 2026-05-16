# 1.
def cek_angka(x):
    if x < 0:
        return   
    print("Angka:", x)

cek_angka(-5)   
cek_angka(10) 

# 2.
def login(otentik):
    if not otentik:
        return   
    print("Selamat datang, pengguna!")

login(False)
login(True)  

# 3.
def luas_persegi(sisi):
    return sisi * sisi   

hasil = luas_persegi(8) 
print("Luas persegi:", hasil)

# 4.
def luas_persegi(sisi):
    return sisi * sisi   

luas_persegi(10)

# 5.
def cek_data(data):
    if not data:
        return None   
    return "Data valid"

print(cek_data(""))  
print(cek_data("Informatika"))

# 6.
def kuadrat_list(data):
    return [x**2 for x in data]

angka = [1, 2, 3, 4]
hasil = kuadrat_list(angka)
print("List asli:", angka)
print("List hasil:", hasil)

# 7.
def penjumlahan_list(lst):
    s = 0

    for elemen in lst:
        s += elemen

    return s

print(penjumlahan_list(7))

# 8.
def buat_list(n):
    return [i for i in range(1, n+1)]

hasil = buat_list(8)
print(hasil)

# 9.
def tahun_kabisat(tahun):
    if tahun % 400 == 0:
        return True
    elif tahun % 100 == 0:
        return False
    elif tahun % 4 == 0:
        return True
    else:
        return False

data_uji = [1900, 2000, 2016, 1987]
data_hasil = [False, True, True, False]

for i in range(len(data_uji)):
    th = data_uji[i]
    print(th, "->", end="")
    hasil = tahun_kabisat(th)
    if hasil == data_hasil[i]:
        print("Ok")
    else:
        print("Gagal")
        
# 10.
def tahun_kabisat(tahun):
    if tahun % 400 == 0:
        return True
    elif tahun % 100 == 0:
        return False
    elif tahun % 4 == 0:
        return True
    else:
        return False


def hari_didalam_bulan(tahun, bulan):
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif bulan in [4, 6, 9, 11]:
        return 30
    elif bulan == 2:
        if tahun_kabisat(tahun):
            return 29
        else:
            return 28

data_uji = [1900, 2000, 2016, 1987]
data_bulan = [2, 2, 1, 11]
data_hasil = [28, 29, 31, 30]

for i in range(len(data_uji)):
    thn = data_uji[i]
    bln = data_bulan[i]
    print(thn, bln, "->", end="")
    hasil = hari_didalam_bulan(thn, bln)
    if hasil == data_hasil[i]:
        print("Ok")
    else:
        print("Gagal")
        
# 11.
def tahun_kabisat(tahun):
    if tahun % 400 == 0:
        return True
    elif tahun % 100 == 0:
        return False
    elif tahun % 4 == 0:
        return True
    else:
        return False

def hari_didalam_bulan(tahun, bulan):
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif bulan in [4, 6, 9, 11]:
        return 30
    elif bulan == 2:
        if tahun_kabisat(tahun):
            return 29
        else:
            return 28
    else:
        return None   

def hari_pada_tahun(tahun, bulan, hari):
    jumlah_hari = hari_didalam_bulan(tahun, bulan)
    if jumlah_hari is None:
        return None
   
    if 1 <= hari <= jumlah_hari:
        return hari
    else:
        return None

print(hari_pada_tahun(2000, 12, 31))  
print(hari_pada_tahun(2000, 2, 30))

# 12.
def cek_prima(bilangan):
    if bilangan <= 1:
        return False
    for i in range(2, int(bilangan**0.5) + 1):
        if bilangan % i == 0:
            return False
    return True

for i in range(1, 20):
    if cek_prima(i + 1):
        print(i + 1, end=" ")
print()

# 13.
def cek_prima(bilangan):
    if bilangan <= 1:
        return False
    for i in range(2, int(bilangan**0.5) + 1):
        if bilangan % i == 0:
            return False
    return True

for i in range(1, 20):
    if cek_prima(i + 1):
        print(i + 1, end=" ")
print()

# 14.
def Liter100km_ke_mpg(liter):
  
    km100 = 100 * 1000
    
    mil = km100 / 1609.344
   
    galon = liter / 3.785411784
    return mil / galon


def mpg_ke_Liter100km(mpg):
   
    km100 = 100 * 1000
  
    mil = km100 / 1609.344
   
    galon = mil / mpg
   
    liter = galon * 3.785411784
    return liter

print(Liter100km_ke_mpg(3.9))
print(Liter100km_ke_mpg(7.5))
print(Liter100km_ke_mpg(10.))
print(mpg_ke_Liter100km(60.3))
print(mpg_ke_Liter100km(31.4))
print(mpg_ke_Liter100km(23.5))
