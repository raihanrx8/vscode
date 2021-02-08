usia = int(input("masukkan usia anda sekarang: "))
tahun = 2020
usia50 = 50 - usia
tahunemas = tahun + usia50
sisa = usia - 50
tahunsisa = 2020 - sisa
if usia < 50:
    print("Usia anda sekarang",usia,"Tahun")
    print("Butuh ",usia50,"Tahun")
    print("Untuk mencapai usia emas di tahun",tahunemas)
if usia > 50:
    print("Usia anda sekarang",usia,"Tahun")
    print("anda telah melewati usia emas", sisa , "tahun lalu")
    print("pada saat tahub", tahunsisa)
if usia == 50:
    print("SELAMAT ANDA BERADA DI USIA EMAS")
    print("Usia anda sekarang",usia,"Tahun")
