data = ["Raihan","Firmansyah"]
data1 = ["ILKKOM","IT"]
data2 = ["UDINUS","FIK"]
data3 = ["Laki","18Tahun"]


# menambah data 
print("-----Fungsi 1-----")
data.append("halo1") 
print (data)

# mehilangkan data yang diinginkan
print("-----Fungsi 2-----")
data.remove("Raihan")
print (data)


# mehilangkan data yang diinginkan berdasarkan urutan urutan
print("-----Fungsi 3-----")
del data[1]


# menggabungkan isi data 1 dan 2
print("-----Fungsi 4-----")
print (data1+data2)

# menggabungkan data dengan data 1
print("-----Fungsi 5-----")
for x in data1:
    data.append(x)
print(data)

# menambahkan informasi sesuai urutan yang diinginkan
print("-----Fungsi 6-----")
data.insert(0,"helllooo")
print (data)


# menggabungkan data 2 dengan data 3
print("-----Fungsi 7-----")
data2.extend (data3)
print(data2)


# merubah urutan dat 3 menjadi terbalik/dari belakang
print("-----Fungsi 8-----")
data3.reverse()
print(data3)




