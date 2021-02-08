
angka1 = int(input("masukan angka pertama :"))
angka2 = int(input("masukan angka kedua   :"))
angka3 = int(input("masukan angka ketiga  :"))
# angka4 = int(input("masukan angka keempat :"))

print("masukan operasi")
print("1 = penjumlahan \n2 = pengurangan ")

ops  = int(input("masukan operasi:"))
ops1 = int(input("masukan operasi:"))
# ops2 = input("masukan operasi:")

if ops == 1:
    hasil = angka1+angka2
elif ops == 2:
    hasil = angka1-angka2
if ops1 == 1:
    hasil  += angka3
elif ops1 == 2:
    hasil  -= angka3
# if ops2 == 1:
#     hasil  += angka4
# elif ops2 == 2:
#     hasil  -= angka4

print("hasil:", hasil)
