kode = int(input("Masukkan Kode baju : "))
ukuran = str(input("Masukkan ukuran baju"))
jumlah = int(input("Masukkan jumlah baju : "))
total_tagihan = 0
pancingan = 0

if kode == 1 :
    print("3second")
    if ukuran == "S" :
        pancingan += 200000
    elif ukuran == "M" :
        pancingan += 220000
    else :
        pancingan += 250000
    if jumlah > 3 :
        print("Harga mendapat diskon 50%" , total_tagihan - int(total_tagihan*0,5))
    elif jumlah < 3 :
        print("Harga baju adalah", total_tagihan)
elif kode == 2 :
    print ("Merk baju adalah Nevada")
    if ukuran == "S" :
        total_tagihan = 170000
    elif ukuran == "M" :
        total_tagihan += 180000
    else :
        total_tagihan += 200000
    if jumlah > 3 :
        print("Harga baju adalah", total_tagihan - ())
elif kode == 3 :
    print("Merk Baju adalah Gucci")
    if ukuran == "S" :
        total_tagihan += 200000
    elif ukuran == "M" :
        total_tagihan += 250000
    else :
        total_tagihan += 270000
    if jumlah > 3:
        print("Harga mendapatkan diskon 40%", total_tagihan - int(total_tagihan * 0,4))
    elif jumlah < 3:
        print("Harga baju adalah", total_tagihan)
elif kode == 4 :
    print("Merk Baju adalah Vitton")
    if ukuran == "S" :
        total_tagihan += 300000
    elif ukuran == "M" :
        total_tagihan += 300000
    else :
        total_tagihan += 350000
    if jumlah > 3:
        print("Harga mendapatkan diskon 35%", total_tagihan - int(total_tagihan * 0,35))
    elif jumlah < 3:
        print("Harga baju adalah", total_tagihan)
elif kode == 5 :
    print("Merk Baju adalah Vitton")
    if ukuran == "S" :
        total_tagihan += 100000
    elif ukuran == "M" :
        total_tagihan += 120000
    else :
        total_tagihan += 130000
    if jumlah > 3:
        print("Harga mendapatkan diskon 45%", total_tagihan - int(total_tagihan * 0,45))
    elif jumlah < 3:
        print("Harga baju adalah", total_tagihan)
else:
    print("Kode anda salah")