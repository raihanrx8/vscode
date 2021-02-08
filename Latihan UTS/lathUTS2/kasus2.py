baris = int(input("Masukkan jumlah baris : "))
kolom = int(input("masukkan jumlah kolom : "))

matrix = []
for i in range(1,baris+1) :
    for j in range (1,kolom+1) :
        inputan = int(input(f"Baris [{i}] Kolom [{j}] : "))
        matrix.append(inputan)


print("Matrixs hasil inputan : ")
n = 0
for x in range(baris) :
    for y in range(kolom) :
        print(matrix[n], end=" ")
        n+=1
    print()
