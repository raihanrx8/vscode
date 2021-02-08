# kamus
x = int(input('Masukkan bilangan : '))
y = int(input('Masukkan bilangan : '))
z= int(input('Masukkan bilangan : '))
# algoritma
for i in range (0,x): #for pertama
    print(" "*(x-i),end="")
    
    for j in range (0,i): #nested for
        print("* ",end="")
    print("")

# algoritma
for i in range (0,y): #for pertama
    print(" "*(y-i),end="")
    
    for j in range (0,i): #nested for
        print("* ",end="")
    print("")

# algoritma
for i in range (0,z): #for pertama
    print(" "*(z-i),end="")
    
    for j in range (0,i): #nested for
        print("* ",end="")
    print("")
