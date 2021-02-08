# kamus
input = str(input('Masukkan inputan : '))
# algoritma
for i in range (len(input)):
    print (' ' * i,end='')
    for j in range(i,len(input)):
        print(input[j],end='')
    print()