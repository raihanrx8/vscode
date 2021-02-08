#kamus
uangjajan = int(input("masukan uang jajan : "))
sisa = uangjajan - 1200000

#algoritma
if(sisa < 500000):
    print("Tidak bisa menonton konser \n karena uang kurang")
elif(sisa < 1000000):
    print("bisa menonton konser \n dengan tempat duduk biasa")
elif(sisa >= 1000000):
    print("bisa menonton konser \n dengan tempat duduk VIP")
    