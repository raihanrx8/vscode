a = []

# membuat inputan 
for i in range(10):
    if a != 0:
        inputan = int(input("Masukkan Bilangan ke-{} : " .format(i+1)))
        a.append(inputan)
        a.sort() # bilangan haris urut
        a = list(dict.fromkeys(a))# output tidak boleh kembar
print(a)

