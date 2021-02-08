#Nomor 1
print('Nomor 1')
x = [7,8,9,1,4,0,3,5,2,6]

for i in range(len(x)):
    if i % 2 == 0 :
        print(x[i+1],end=' ')
    else:
        print(x[i-1],end=' ')
print()
print('=====================')
#Nomor 2
print('Nomor 2')
bulan = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']
print('Penentuan nama bulan')
print('--------------------')
kodebulan=int(input('Kode Bulan(1...12): '))
if kodebulan < 1 or kodebulan > 12:
    print('Kode bulan harus antara 1 sampai 12')
else:
    print('Bulan',bulan[kodebulan - 1])

print('=====================')
#Nomor 3
print('Nomor 3')
print('Masukkan 10 data bilangan bulat')
x = []
for i in range(10):
    y=int(input('Bilangan {} - '.format(i+1)))
    x.append(y)
rata2=sum(x)/len(x)
print('Rata-rata = ',rata2)
print('Daftar Nilai di atas rata-rata')
for i in x:
    if i > rata2:
        print(i)
print('=====================')
#Nomor 4
print('Nomor 4')
jum_data=10
data=[77,48,2,23,33,45,56,0,86,71]
print('Pencarian Data')
print('==============')
dicari = int(input('Data yang dicari: '))

#Pencarian data
posisi=-1
for i in range(0,jum_data):
    if data[i] == dicari:
        posisi = i
        break

if posisi == -1:
    print('Data tidak ditemukan')
else:
    print('Data ditemukan. Posisi pada index',posisi)