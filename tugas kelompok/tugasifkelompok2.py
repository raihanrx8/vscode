ekskul = input("masukan ekskul pilihan: \n[basket/voli]")
jeniskelamin = input("masukan jenis kelamin: \n[pria/wanita]")


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
    def hari(i):
     switcher={
          0:'senin',
          1:'selasa',
          2:'rabu',
          3:'kamis'
     }
     return switcher.get(i, "tidak ada hari")
print(hari(2))
    

#print("harap isi data sesuai format \nterima kasih")