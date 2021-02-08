insertbaris = int(input("Masukkan Baris : "))
insertkolom = int(input("Masukkan kolom : "))
matrix_a = []
matrix_b = []

def cetak_matrix(matrix):
    for row in matrix:
        print(row)

# def panjang_matrix(matrix):
#     return len(matrix[0])

# def lebar_matrix(matrix):
#     return len(matrix)


for i in range(insertbaris):
    a = []
    for j in range(insertkolom):
        insertvalue = int(input(" Matrix A Baris ke-{} Kolom ke-{} : " .format(i+1,j+1)))
        a.append(insertvalue)
    matrix_a.append(a)
print()

for i in range(insertbaris):
    b = []
    for j in range(insertkolom):
        insertvalue = int(input(" Matrix b Baris ke-{} Kolom ke-{} : " .format(i+1,j+1)))
        b.append(insertvalue)
    matrix_b.append(b)
print()


print("Hasil Matrix A")
cetak_matrix(matrix_a)


print("Hasil Matrix B")
cetak_matrix(matrix_b)


for x in range(insertbaris):
    for y in range(insertkolom):
        c = (matrix_a[x][y] + matrix_b[x][y])
        print(c,end=" ")
    print()
print()



