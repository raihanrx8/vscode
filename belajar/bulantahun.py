hari = int(input("Masukkan Hari :" ))


sisa_tahun = int(hari%365)
tahun = int(hari/365)
sisa_bulan = int(sisa_tahun%30)
bulan = int(sisa_tahun/30)
sisa_minggu = int(sisa_bulan%7)
minggu = int(sisa_bulan/7)
# sisa_hari = int(hari%7)
# hari = int(sisa_minggu)



# print(sisa_tahun)
print(tahun,"Tahun")
# print(sisa_bulan)
print(bulan,"Bulan")
print(sisa_minggu,"Hari")
print(minggu,"Minggu")
# print(sisa_hari)
# print(hari,"Hari")
# print(tahun)
print(tahun,"Tahun",bulan,"Bulan",minggu,"Minggu",sisa_minggu,"Hari")