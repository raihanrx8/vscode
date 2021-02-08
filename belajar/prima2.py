# menentukan bilangan Prima
num = int(input('Masukkan bilangan : '))
# bilangan prima harus lebih besar dari 1
if num > 1:
    for i in range(2,num) :
        if (num % i) == 0 :
            print(num, 'Bukan bilangan prima')
            print(i, 'kali',num//i,'=',num)
            break
    else:
         print(num,'Adalah bilangan prima')
else:
    print(num,'Bukan bilangan prima')