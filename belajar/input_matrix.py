x = int(input(" Masukkan Jumlah Baris : "))
y = int(input(" Masukkan Jumlah kolom : "))
z = []

# buat inputan matrix
for x in range (1,x+1):
    for y in range (1,y+1):
        baris = int(input(f" baris [{x}] kolom [{y}] :"))
        z.append(baris)
        # print(z)     
         
n = 0
for i in range (0,x):
    for j in range (0,y):
        print(z[n], end=" ")
        n+=1
    print()

