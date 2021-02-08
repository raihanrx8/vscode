ekskul = input("masukan ekskul pilihan: \n[basket/voli]")
jeniskelamin = input("masukan jenis kelami: \n[pria/wanita]")


if (ekskul=="basket"):
    print("semua berkumpul di lapangan basket")
    if (jeniskelamin=="pria"):
        print("titik kumpul di lapangan outdoor")
    else:
        print("titik kumpul di lapangan indoor")

elif (ekskul=="voli"):
    print("semua berkumpul di lapangan voli")
    if (jeniskelamin=="pria"):
        print("titik kumpul jam 5 sore")
    else:
        print("titik kumpul jam 9 pagi")
else:
    print("harap isi data sesuai format \nterima kasih")

