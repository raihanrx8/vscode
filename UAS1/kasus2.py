jum_data = int(input("Masukkan Baris : "))
a = []

for i in range(jum_data):
    data = int(input("Masukkan inputan data ke-{} : ".format(i+1)))
    a.append(data)
print(a)

dicari = int(input("Masukkan Data yang ingin dicari : "))

#Pencarian data
posisi=-1
for i in range(0,jum_data):
    if a[i] == dicari:
        posisi = i
        break

if posisi == -1:
    print('Data tidak ditemukan')
    print(posisi)
else:
    print('Data ditemukan. Posisi pada index',posisi+1)

