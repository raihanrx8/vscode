#tugas daspro
#input variable
ekskul = input("masukan ekskul pilihan: \n[basket/voli]")
jeniskelamin = input("masukan jenis kelamin: \n[pria/wanita]")
pilihhari = print("masukan tanggal ekskul")
#input switch case
#pemilihan hari berdasarkan tanggal
def hari(i):
     switcher={
          1:'senin',
          2:'selasa',
          3:'rabu',
          4:'kamis',
          5:'jumat',
          6:'sabtu',
          7:'minggu',
          8:'senin',
          9:'selasa',
          10:'rabu',
          11:'kamis',
          12:'jumat',
          13:'sabtu',
          14:'minggu',
          15:'senin',
          16:'selasa',
          17:'rabu',
          18:'kamis',
          19:'jumat',
          20:'sabtu',
          21:'minggu',
          22:'senin',
          22:'selasa',
          23:'rabu',
          24:'kamis',
          25:'jumat',
          26:'sabtu',
          27:'minggu',
          28:'senin',
          29:'selasa',
          30:'rabu',
          31:'kamis'

     }
     return switcher.get(i, "tidak ada")
n = int(input(" [1-31] : "))
print("Hari", hari(n))


#if,elif,else,nested if
if (ekskul=="basket"):
    print("semua berkumpul di lapangan basket")
    if (jeniskelamin=="pria"):
        print("tempat kumpul : lapangan outdoor")
    else:
        print("tempat kumpul : lapangan indoor")

elif (ekskul=="voli"):
    print("semua berkumpul di lapangan voli")
    if (jeniskelamin=="pria"):
        print("jam kumpul : jam 5 sore")
    else:
        print("jam kumpul jam 9 pagi")
else:
    print("harap isi data sesuai format \nterima kasih")