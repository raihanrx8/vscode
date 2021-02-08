jumlah = int(input("Masukkan Jumlah n : "))
print("Masukkan Nilai-nilai List A dan B")
a = [int(input(f'List A ke-{i} : ')) for i in range(1, jumlah+1)]
print()
b = [int(input(f'List B ke-{i} : ')) for i in range(1, jumlah+1)]
irisan = []
for i in range(jumlah):
    if a[i] in b:
        if a[i] not in irisan:
            irisan.append(a[i])
irisan.sort()
genap = [i for i in range(max(irisan)+1) if i in irisan if i%2==0]
ganjil = [i for i in range(max(irisan)+1) if i in irisan if i%2!=0]
print(f'a : {a}')
print(f'b : {b}')
print(f'Nilai-nilai yang beririsan :{",".join("{}".format(n) for n in irisan)} ' )
print(f'jumlah nilai irisan genap :{"+".join("{}".format(n) for n in genap)} = {sum(genap)}')
print(f'jumlah nilai irisan genap :{"+".join("{}".format(n) for n in ganjil)} = {sum(ganjil)}')
print(f'total genap+ganjil = {sum(genap)} + {sum(ganjil)} = {sum(irisan)}')