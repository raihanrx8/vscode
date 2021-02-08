x = int(input("Masukkan jumlah list : "))

a = []
b = []
irisan = []
ganjil = []
genap = []

for i in range(x):
    inputan = int(input("Masukkan Nilai A ke-{} : " .format(i+1)))
    a.append(inputan)

print("="*20)

for i in range(x):
    inputan = int(input("Masukkan Nilai B ke-{} : " .format(i+1)))
    b.append(inputan)

for j in a:
    for k in b:
        if j==k:
            irisan.append(j)
            irisan = list(dict.fromkeys(irisan))# output tidak boleh kembar
print(irisan)

#algoritma untuk menentukan bil negatif/positif

print("genap")
for i in irisan:
    if i%2 == 0:
        genap.append(i)
print(genap)
jml_genap = sum(genap)
print("Jumlah Genap : ", jml_genap)


print("ganjil")
for j in irisan:    
    if j%2 != 0:
        ganjil.append(j)
print(ganjil)
jml_ganjil = sum(ganjil)
print("Jumlah Ganjil : ", jml_ganjil)

total = jml_genap + jml_ganjil
print("Total Jumlah Genap dan Ganjil : " , total)




