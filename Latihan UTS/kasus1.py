# kamus
angka1 = int(input("Masukan nilai Pertama : "))
if angka1 > 100:
    print("input tidak boleh melebihi 100")
    quit()
angka2 = int(input("Masukan nilai Kedua : "))
if angka1 > 100:
    print("input tidak boleh melebihi 100")
    quit()
angka3 = int(input("Masukan nilai Ketiga : "))
if angka1 > 100:
    print("input tidak boleh melebihi 100")
    quit()


print("opsi 1 untuk penjumlahan \nopsi 2 untuk pengurangan")

ops1 = int(input("Masukan jenis operasi : [1/2] "))
ops2 = int(input("Masukan jenis operasi : [1/2] "))

# ops1
hasil1 = angka1+angka2
hasil2 = angka1-angka2
# ops2
hasil3 = hasil1+angka3
hasil4 = hasil1-angka3
hasil5 = hasil2+angka3
hasil6 = hasil2-angka3

if ops1 == 1:
    # hasil3
    if ops2 == 1:
        print(hasil3)
        if hasil3%2==0:
            print("Genap")
            if hasil3<0:
                print("negatif")
            elif hasil3>=0:
                print("positif")
        else:
            print("ganjil")
            if hasil3<0:
                print("negatif")
            elif hasil3>=0:
                print("positif")
    # hasil4
    if ops2 == 2:
        print(hasil4)
        if hasil4%2==0:
            print("Genap")
            if hasil4<0:
                print("negatif")
            elif hasil4>=0:
                print("positif")
        else:
            print("ganjil")
            if hasil4<0:
                print("negatif")
            elif hasil4>=0:
                print("positif")

if ops1 == 2:
    #hasil5
    if ops2 == 1:
        print(hasil5)
        if hasil5%2==0:
            print("Genap")
            if hasil5<0:
                print("negatif")
            elif hasil5>=0:
                print("positif")
        else:
            print("ganjil")
            if hasil5<0:
                print("negatif")
            elif hasil5>=0:
                print("positif")

    #hasil6
    if ops2 == 2:
        print(hasil6)
        if hasil6%2==0:
            print("Genap")
            if hasil6<0:
                print("negatif")
            elif hasil6>=0:
                print("positif")
        else:
            print("ganjil")
            if hasil6<0:
                print("negatif")
            elif hasil6>=0:
                print("positif")
            



#algoritma untuk menentukan bil ganjil/positif





