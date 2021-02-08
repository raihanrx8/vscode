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
    print(posisi)
else:
    print('Data ditemukan. Posisi pada index',posisi)



#     jumlah = 10
# list = [1,2,3,4,5,6,7,8,9,10]
# i = 0
# data = int(input("Masukkan Data yang ingin dicari : "))
# for i in list:
#     if list[i] == data:
#         posisi = i
#         break
  
# for x in list:
#     if data == x:
#         print("ada", i)
#         break
#     else:
#         print("tidak ada")
