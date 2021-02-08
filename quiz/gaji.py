nama = input("masukan Nama : ")
NIK = int(input("masukan NIK:"))
statusKaryawan = str(input("masukan status karyawan: \n[ tetap/honorer] : "))
golongan = int(input("masukan golongan:[1/2/3]:"))


if (statusKaryawan == "tetap" )
    print("Gaji pokok : 2.000.000")
'''    if (golongan=="1"):
        print("bonus anda : 200.000")
    elif (golongan=="2"): 
        print("bonus anda : 350.000")
    elif (golongan=="3"):
        print("bonus anda : 500.000")
    
elif (statusKaryawan=="honorer"):
    print("Gaji pokok : 1.000.000")
    if (golongan=="1"):
        print("bonus anda : 100.000")
    elif (golongan=="2"): 
        print("bonus anda : 150.000")
    elif (golongan=="3"):
        print("bonus anda : 300.000")
    
else:
    print("harap isi data sesuai format \nterima kasih")

