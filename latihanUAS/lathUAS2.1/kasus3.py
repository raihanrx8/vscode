baris = int(input("Masusukkan Baris : "))
kolom = int(input("Masusukkan Kolom : "))
matrix_a = []
matrix_b = []

def panggil_matrix(matrix):
    for row in matrix:
        print(row)

print("=====MATRIX A=====")
for i in range(baris):
    a = []
    for j in range(kolom):
        inputan = int(input(" MATRIX A Baris ke-{} Kolom ke-{} : " .format(i+1,j+1)))
        a.append(inputan)
    matrix_a.append(a)
print()


print("=====MATRIX B=====")
for i in range(baris):
    b = []
    for j in range(kolom):
        inputan = int(input(" MATRIX B Baris ke-{} Kolom ke-{} : " .format(i+1,j+1)))
        b.append(inputan)
    matrix_b.append(b)
print()

print("=====MATRIX A=====")
panggil_matrix(matrix_a)

print("=====MATRIX B=====")
panggil_matrix(matrix_b)



for x in range(baris):
    for y in range(kolom):
        c = (matrix_a[x][y] + matrix_b[x][y])
        print(c,end=" ")
    print()
print()




