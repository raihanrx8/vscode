x = int(input("Masukan Angka :"))


for i in reversed(range(1,x+1)):
    for j in range (1,i+1):
        print(j,end=" ")
    print()

print("--------------------")

for i in range(1,x+1):
    while i<=x:
        print(i,end=" ")
        i+=1
    print("")
  