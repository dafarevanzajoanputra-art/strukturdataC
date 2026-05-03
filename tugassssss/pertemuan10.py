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