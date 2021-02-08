a = [[1,2,3,],
    [4,5,6,],
    [7,8,9],
    [1,2,3,],
    [4,5,6,],
    [7,8,9]]


# mengambil list pertama
print("-"*30)
print(a[0])


# mengambil list kedua
print("-"*30)
print(a[1])


# mengambil list ketiga
print("-"*30)
print(a[2])


# mengambil list dalam list
print("-"*30)
print(a[0][1])


# mengambil list dalam list
print("-"*30)
print(a[1][2])


# mengambil list dalam list
print("-"*30)
print(a[2][1])



print("-"*30)
angka = a.copy() #angka = a tapi a tidak= angka. karna ada copy()
angka.append("Haloo haloo ")
print(angka)


# mengubah list menjadi loop
print("-"*30)
for i in  a:
    for j in  i:
        print(j, end="  ")
    print()


# mengubah struktur baris menjadi banjar
print("-"*30)
for record in a: 
    print(record) 

