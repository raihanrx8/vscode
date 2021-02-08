# kamus
x= int(input('Masukkan bilangan : '))
# algoritma

# for i in range (0,x):
#     for j in  range(0,i+1):
#         print("*",end="")
#     print()

for i in range (0,x):
    print(" "*(i),end="")
    
    for j in range(0,x):
        print("* "*(j-1),end="")
    print("")

   
