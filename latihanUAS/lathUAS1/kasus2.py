bulan = ['nol','Januari','Februari','Maret','April',
        'Mei','Juni','Juli','Agustus',
        'September','Oktober','November','Desember']

print("Penentuan nama bulan")
print("-"*30)

a = int(input("Masukan nomer bulan 1 - 12 : "))

if a <= 12:
    print(bulan[a])
else:
    print("Kode bulan harus antara 1 - ")