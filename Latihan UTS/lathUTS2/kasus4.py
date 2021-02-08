baris = int(input("Masukkan jumlah baris : "))
kolom = int(input("masukkan jumlah kolom : "))

matrix = []
for i in range(1,baris+1) :
    for j in range (1,kolom+1) :
        inputan = int(input(f"Masukkan array [{i}] [{j}] : "))
        matrix.append(inputan)


print("Matrixs hasil inputan : ")
n = 0
for x in range(baris) :
    for y in range(kolom) :
        print(matrix[n], end=" ")
        n+=1
    print()

if kolom % 2 == 0 :
    data = []
    indexganjil = 0
    for a in range(baris) :
        hasil = matrix[indexganjil]
        indexganjil += 2
        data.append(hasil)
else :
    data = []
    indexganjil = 0
    for a in range(baris) :
        for b in range (0,kolom,2) :
            hasil = matrix[indexganjil]
            indexganjil += 2
            data.append(hasil)
        indexganjil -= 1

print(f"Nilai terbesar kolom ganjil : {max(data)}")
print(f"Nilai terkecil kolom ganjil : {min(data)}")