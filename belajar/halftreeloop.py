# kamus
print("Segitiga Vertikal")

x = int(input("Masukan batas akhir output : "))
# program
for i in range (0,x):
    for j in  range(0,i+1):
        print("*",end="")
    print()

for i in reversed(range (0,x)):
# melalakukan kebalikannya
    for j in  range(1,i+1):
        print("*",end="")
    print()