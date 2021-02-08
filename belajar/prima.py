n = int(input("Masukan angka :" ))

if n > 1:
    for i in range(2,n):
        if (n%i) == 0:
            print("Bukan Prima")
            break
        else:
            print("bilangan Prima")
            break
else:
    print("Bukan Prima")
