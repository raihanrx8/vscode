x = int(input("Masukkan lebar : "))
y = int(input("Masukkan panjang : "))

for i in range(0,x,1):
    for j in range(0,y,1):
        if (i==0) or (i==x-1) or (j==0) or (j==y-1):
            print("*", end=" ")
        else:
            print(" ", end=" "),
    print("")
print()
]
