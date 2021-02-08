# kamus

print("====================")
nama = str(input("Masukkan Nama :"))
ipk = int(input("Masukkan IPK :"))
akreditasi = str(input("Masukkan Akreditasi Universitas :"))
print("====================")
if ipk > 3 and akreditasi == "a" :
    print("Pelamar lulus babak 1")
    print("Silahkan masukkan nilai ")
    ta = int(input("Masukkan nilai Test Akademik     :")) 
    tk = int(input("Masukkan nilai Test Keterampilan :")) 
    tp = int(input("Masukkan nilai Test psikologi    :")) 
    rata2 = int((ta+tk+tp)/3)
# print("====================")

    if rata2 >= 85 and (ta or tk or tp) >= 80:
        print("Pelamar lulus babak 2")
        if ta>=tk and ta>=tp:
            print("Nilai Rata-rata   :", rata2)
            print("Anda diterima di bagian Manajemen")
        elif tk>=ta and ta>=tp:
            print("Nilai Rata-rata   :", rata2)
            print("Anda diterima di bagian Produksi")
        else:
            print("Nilai Rata-rata   :", rata2)
            print("Anda diterima di bagian Pemasaran")
    else:
        print("Pelamar tidak lulus babak 2")
else:
    print("Pelamar tidak lulus babak 1")
        

# print("====================")
# print("Nama   :", nama)
# print("IPK    :", ipk)
# print("Akreditasi Universitas   :", akreditasi)
# print("Test Akademik   :", ta)
# print("Test Ketrampilan   :", tk)
# print("Test Psikologi   :", tp)



