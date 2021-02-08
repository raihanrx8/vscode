x = int(input("Masukkan jumlah list : "))

a = []
b = []
irisan = []


for i in range(x):
    inputan = int(input("Masukkan Nilai A ke-{} : " .format(i+1)))
    a.append(inputan)

print("="*20)

for i in range(x):
    inputan = int(input("Masukkan Nilai B ke-{} : " .format(i+1)))
    b.append(inputan)



for j in a:
    for k in b:
        if j==k:
            print(j)
            irisan.append(j)
print(irisan)
            


#             c = []
#             c.append(j)
#             c = list(dict.fromkeys(a))# output tidak boleh kembar
# print(c)

# jumlah = sum(c)
# print("Isi list :" ,c)
# print("hasil penjumlahan list :", jumlah)
    