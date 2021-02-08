x = int(input("Masukan batas akhir output : "))

# for i in range (0,x):
#     for j in  range(0,i+1):
#         print("*",end="")
#     print()

# for i in reversed(range (0,x)):
#     for j in  range(1,i+1):
#         print("*",end="")
#     print()

for i in range(1,x):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
print("_____-------______")

for i in reversed(range(1,x+1)):
    for j in range(1,i+1):
        print(j,end=" ")
    print()