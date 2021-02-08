# kamus
print("          PROGRAM PENJUALAN SUSU")
nama =       str(input("masukan nama          : "))
kodesusu =   int(input("masukan kode susu     : [1/2/3]"))
kodeukuran = str(input("masukan kode ukuran   : [S/M/L]"))
jumlahbeli = int(input("masukan jumlah beli   : "))


if kodesusu == 1:
    print("merk barang : Susu Indomilk")
    if kodeukuran == "S" :
        print("Jenis ukuran : Small ")
        harga = 5000
    elif kodeukuran == "M" :
        print("Jenis ukuran : Medium  ")
        harga =7500
    elif kodeukuran == "L" :
        print("Jenis ukuran : Large  ")
        harga =9500

elif kodesusu == 2:
    print("merk barang : Susu Dancow")
    if kodeukuran == "S" :
        print("Jenis ukuran : Small  ")
        harga =4500
    elif kodeukuran == "M" :
        print("Jenis ukuran : Medium ")
        harga =6500 
    elif kodeukuran == "L" :
        print("Jenis ukuran : Large  ")
        harga =8500
elif kodesusu == 3:
    print("merk barang : Susu Sustagen")
    if kodeukuran == "S" :
        print("Jenis ukuran : Small ")
        harga =9500
    elif kodeukuran == "M" :
        print("Jenis ukuran : Medium ")
        harga =15500 
    elif kodeukuran == "L" :
        print("Jenis ukuran : Large  ")
        harga =19500

print("          STRUK PEMBAYARAN")
print("Nama pembeli          :",nama )
print("Merk barang           :",kodesusu)
print("Jenis Ukuran          :",kodeukuran)
print("Jumlah Beli           :",jumlahbeli)
jumlahbayar = harga*jumlahbeli
print("Jumlah Pembayaran     :",jumlahbayar)
if jumlahbeli > 25:
    potongan = 5/100*jumlahbayar  
    str(print("Potongan              :",potongan))
pajak = 10/100*jumlahbayar
str(print("Pajak                 :",pajak))
totalbayar = jumlahbayar+pajak-potongan
str(print("Total Pembayaran      :",totalbayar))