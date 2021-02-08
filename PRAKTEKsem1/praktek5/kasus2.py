print("selamat datang \n di penukaran motor honda")
tahun = int(input("masukan tahun produksi motor : "))
kekurangan = ( 2020 - tahun) * 2000000
if tahun >= 2020:
    print("Motor sudah tahun 2020")
else:
    print("dikenakan biaya tambahan sebesar : \n" ,kekurangan)