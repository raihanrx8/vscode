
# kamus
print("-------Penjualan Produk-------")
print("pilih kode sesuai produk")
print("1 = 3second \n2 = Nevada \n3 = Gucci \n4 = Louis Vuitton \n5 = Kick Denim")
kode   = int(input("Masukkan kode   : " ))
print("s = small \nm = medium \ndan lain lain")
ukuran =     input("Masukkan ukuran : " )
print("beli lebih dari 3 \nakan mendapat potongan harga")
jumlah = int(input("Masukkan jumlah :"))
if kode == 1:
    nama = "3second"
    if ukuran == "s" :
        if jumlah > 3:
            harga = 200000
            totalpembayaran = int(harga*jumlah*0.5)
        elif jumlah <= 3:
            harga = 200000
            totalpembayaran = harga*jumlah
    elif ukuran == "m" :
        if jumlah > 3:
            harga = 220000
            totalpembayaran = int(harga*jumlah*0.5)
        elif jumlah <= 3:
            harga = 220000
            totalpembayaran = harga*jumlah
    else:
        if jumlah > 3:
            harga = 250000
            totalpembayaran = int(harga*jumlah*0.5)
        elif jumlah <= 3:
            harga = 250000
            totalpembayaran = harga*jumlah
        
if kode == 2:
    nama = "Nevada"
    if ukuran == "s" :
        if jumlah > 3:
            harga = 170000
            totalpembayaran = int(harga*jumlah*0.5)
        elif jumlah <= 3:
            harga = 170000
            totalpembayaran = harga*jumlah
    elif ukuran == "m" :
        if jumlah > 3:
            harga = 180000
            totalpembayaran = int(harga*jumlah*0.5)
        elif jumlah <= 3:
            harga = 180000
            totalpembayaran = harga*jumlah
    else:
        if jumlah > 3:
            harga = 200000
            totalpembayaran = int(harga*jumlah*0.5)
        elif jumlah <= 3:
            harga = 200000
            totalpembayaran = harga*jumlah
        
if kode == 3:
    nama = "Gucci"
    if ukuran == "s" :
        if jumlah > 3:
            harga = 200000
            totalpembayaran = int(harga*jumlah*0.4)
        elif jumlah <= 3:
            harga = 200000
            totalpembayaran = harga*jumlah
    elif ukuran == "m" :
        if jumlah > 3:
            harga = 250000
            totalpembayaran = int(harga*jumlah*0.4)
        elif jumlah <= 3:
            harga = 250000
            totalpembayaran = harga*jumlah
    else:
        if jumlah > 3:
            harga = 270000
            totalpembayaran = int(harga*jumlah*0.4)
        elif jumlah <= 3:
            harga = 270000
            totalpembayaran = harga*jumlah
        
if kode == 4:
    nama = "Louis Vuitton"
    if ukuran == "s" :
        if jumlah > 3:
            harga = 300000
            totalpembayaran = int(harga*jumlah*0.35)
        elif jumlah <= 3:
            harga = 300000
            totalpembayaran = harga*jumlah
    elif ukuran == "m" :
        if jumlah > 3:
            harga = 300000
            totalpembayaran = int(harga*jumlah*0.35)
        elif jumlah <= 3:
            harga = 300000
            totalpembayaran = harga*jumlah
    else:
        if jumlah > 3:
            harga = 350000
            totalpembayaran = int(harga*jumlah*0.35)
        elif jumlah <= 3:
            harga = 350000
            totalpembayaran = harga*jumlah
        
if kode == 5:
    nama = "Kick Denim"
    if ukuran == "s" :
        if jumlah > 3:
            harga = 100000
            totalpembayaran = int(harga*jumlah*0.45)
        elif jumlah <= 3:
            harga = 100000
            totalpembayaran = harga*jumlah
    elif ukuran == "m" :
        if jumlah > 3:
            harga = 120000
            totalpembayaran = int(harga*jumlah*0.45)
        elif jumlah <= 3:
            harga = 120000
            totalpembayaran = harga*jumlah
    else:
        if jumlah > 3:
            harga = 130000
            totalpembayaran = int(harga*jumlah*0.45)
        elif jumlah <= 3:
            harga = 130000
            totalpembayaran = harga*jumlah
        

print ("-------Struk Pembayaran-------")
print ("Nama Produk      : " , nama)
print ("Ukuran Produk    : " , ukuran)
print ("Jumlah Produk    : " , jumlah)
print ("total pembayaran : " , totalpembayaran)