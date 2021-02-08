bil1 = int(input("Masukan Bilangan Pertama : "))
bil2 = int(input("Masukan Bilangan Kedua : "))


def tambah(bil1,bil2):
    total = bil1 + bil2
    print(bil1 ,"+", bil2 ,"=", total)
    return total

a = tambah(bil1,bil2)
print(a)

print("="*20)

def tambah(bil1,bil2):
    return bil1 + bil2

print(tambah(bil1,bil2))

