jumlah = int(input("Masukkan jumlah Nama : "))
anak = []

for i in range(0,jumlah):
    nama = str(input(f'Masukkan Nama {i+1} : '))
    anak.append(nama)
print(anak)
    

for i in range(0,len(anak)):
    print(f'{i+1}. Hai {anak[i]}')
