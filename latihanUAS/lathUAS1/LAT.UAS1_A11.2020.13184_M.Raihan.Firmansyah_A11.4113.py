
print("-"*10,"Kasus 1","-"*10)
#Nomor 1
# kamus
print('Nomor 1')
a = [7,8,9,1,4,0,3,5,2,6]
# algorima
print(a[1],a[0],a[3],a[2],a[5],a[4],a[7],a[6],a[9],a[8])


print("-"*10,"Kasus 2","-"*10)
#Nomor 2
# kamus
print('Nomor 2')
bulan = ['nol','Januari','Februari','Maret','April',
        'Mei','Juni','Juli','Agustus',
        'September','Oktober','November','Desember']

print("Penentuan nama bulan")
print("-"*30)
# algoritma
a = int(input("Masukan nomer bulan 1 - 12 : "))

if a <= 12:
    print(bulan[a])
else:
    print("Kode bulan harus antara 1 - ")



print("-"*10,"Kasus 2","-"*10)
#Nomor 3
# kamus
print('Nomor 3')
x = []
for i in range (10):
    y = int(input("Masukan bilangan {} :" .format(i+1)))
    x.append(y)
rata = sum(x)/len(x)
print("Rata - rata :", rata)
print("Daftar nilai diatas rata rata")
# algoritma
for i in x:
    if i > rata:
        print(i)


print("-"*10,"Kasus 2","-"*10)
#Nomor 4
# kamus
print('Nomor 4')
jumlahdata=10
data = [77,48,2,23,33,45,56,0,86,71]
print('Pencarian Data')
print("-"*15)
dicari = int(input('Data yang dicari: '))

#Pencarian data
posisi = -1
for i in range(0,jumlahdata):
    if data[i] == dicari:
        posisi = i
        break

if posisi == -1:
    print('Data tidak ditemukan')
else:
    print('Data ditemukan. Posisi pada index',posisi)