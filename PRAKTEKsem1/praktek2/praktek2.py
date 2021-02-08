print("---------------kasus 1---------------")
#initialisasi variable dan tipe data
a = 0
b = 4.5
c = 'kata'
print("latihan 1 \n")
print (type(a))
print("\tnilai bilangan bulat a adalah",a,"\n")
print (type(b))
print("\tnilai bilangan decimal a adalah",b,"\n")
print (type(c))
print("\tkata dari c adalah",c,"\n")

print("---------------kasus 2---------------")
#initialisasi variable dan tipe data
umur = 18 
beratbadan = 48.3
#contoh output program dengan variable print
print("umur saya",umur,"tahun")
print("umur saya",umur,)
print("umur saya"+str(umur)+"tahun")
print("umur saya %d" % (umur))
print("berat badan saya %f" % (beratbadan))
print("berat badan saya {} kilogram".format(beratbadan))

print("---------------kasus 3---------------")
#kamus
ayah = "joko"
ibu = "surti"
print("nama ayah mawar adalah",ayah,"\n")
print("nama ibu mawar adalah",ibu,"\n")

print("---------------kasus 4---------------")
#kamus
a = 1
b = 4
#algoritma
print("hasil a yang pertama:",a)
print("hasil b yang pertama: "+str(b))
b = a  #algoritma 2
a -= b #  a = a - b
print("hasil a yang kedua: "+str(a))
print("hasil b yang kedua:",b )
a = b + 2  
b = a * b
print("hasil a yang ketiga: {}".format(a))
print("hasil b yang ketiga %f" % (b))
#cara menukar nilai pada dua variable
c = a
a = b
b = c
print("hasil a yang keempat: {}".format(a))
print("hasil b yang keempat: {}".format(b))
