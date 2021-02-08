def tambah(a,b):
    return a+b

def kurang(a,b):
    return a-b

def kali(a,b):
    return a*b

def bagi(a,b):
    return a/b

print("Pilih operator")
print("+")
print("-")
print("*")
print("/")

A = int(input('Angka pertama:'))
pilihan = input('Operator digunakan :')
B = int(input('Angka kedua:'))

if pilihan == '+':
    print(A,'+',B,'=', tambah(A,B))
elif pilihan == '-':
    print(A,'-',B,'=', kurang(A,B))
elif pilihan == '*':
    print(A,'*',B,'=', kali(A,B))
elif pilihan == '/':
    print(A,'/',B,'=', bagi(A,B))
else:
    print('Invalid input')

