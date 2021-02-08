n = int(input("Masukan nilai prima : "))
arrprima = [2]

if n > 1:
    for i in range(3,n+1,4):
        for j in range (2,i+1):
            if i%j ==0:
                break
            elif i-1==j:
                arrprima.append(i)
                break
    for k in arrprima:
        print(k, end=" ")

else:
    print("tidak prima")