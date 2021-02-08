kode = int(input("masukan kode baju :"))
ukuran = str(input("masukan ukuran baju :"))
jumlahbeli = int(input("masukan jumlah beli baju :"))

if kode == 1:
    print("merk baju : 3second")
    if ukuran == "s":
        print("Ukuran baju : S")
        harga = 200000
        if jumlahbeli > 3:
            potongan = harga*50/100
        else:
            potongan=harga
    elif ukuran == "m":
        print("Ukuran baju : M")
        harga = 220000
        if jumlahbeli > 3:
            potongan = harga*50/100
        else:
            potongan=harga
    else:
        print("Ukuran baju : selain S dan M")
        harga = 250000
        if jumlahbeli > 3:
            potongan = harga*50/100
        else:
            potongan=harga


elif kode == 2:
    print("merk baju : Nevada")
    if ukuran == "s":
        print("Ukuran baju : S")
        harga = 170000
        if jumlahbeli > 3:
            potongan = harga*50/100
        else:
            potongan=harga
    elif ukuran == "m":
        print("Ukuran baju : M")
        harga = 180000
        if jumlahbeli > 3:
            potongan = harga*50/100
        else:
            potongan=harga
    else:
        print("Ukuran baju : selain S dan M")
        harga = 200000
        if jumlahbeli > 3:
            potongan = harga*50/100
        else:
            potongan=harga


elif kode == 3:
    print("merk baju : Gucci")
    if ukuran == "s":
        print("Ukuran baju : S")
        harga = 200000
        if jumlahbeli > 3:
            potongan = harga*50/100
        else:
            potongan=harga
    elif ukuran == "m":
        print("Ukuran baju : M")
        harga = 250000
        if jumlahbeli > 3:
            potongan = harga*50/100
        else:
            potongan=harga
    else:
        print("Ukuran baju : selain S dan M")
        harga = 270000
        if jumlahbeli > 3:
            potongan = harga*50/100
        else:
            potongan=harga


elif kode == 4:
    print("merk baju : Louis Vuitton")
    if ukuran == "s":
        print("Ukuran baju : S")
        harga = 300000
        if jumlahbeli > 3:
            potongan = harga*50/100
        else:
            potongan=harga
    elif ukuran == "m":
        print("Ukuran baju : M")
        harga = 300000
        if jumlahbeli > 3:
            potongan = harga*50/100
        else:
            potongan=harga
    else:
        print("Ukuran baju : selain S dan M")
        harga = 350000
        if jumlahbeli > 3:
            potongan = harga*50/100
        else:
            potongan=harga



elif kode == 5:
    print("merk baju : kick denim")
    if ukuran == "s":
        print("Ukuran baju : S")
        harga = 100000
        if jumlahbeli > 3:
            potongan = harga*50/100
        else:
            potongan=harga
    elif ukuran == "m":
        print("Ukuran baju : M")
        harga = 120000
        if jumlahbeli > 3:
            potongan = harga*50/100
        else:
            potongan=harga
    else:
        print("Ukuran baju : selain S dan M")
        harga = 130000
        if jumlahbeli > 3:
            potongan = harga*50/100
        else:
            potongan=harga

else:
    print("kode tidak tercantum")

print("-------struk pembayaran-------")
print("Merk baju :", kode)
print("Ukuran baju :", ukuran)
print("Jumlah beli baju :", jumlahbeli)

total = harga*jumlahbeli
totalproduk =potongan*jumlahbeli
if jumlahbeli > 3:
    (print("total pembayaran :",totalproduk))
else:
    print("total pembayaran :",total)
