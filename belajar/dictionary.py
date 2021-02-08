# LATIHAN DICTIONARY SIMPLE
# bentuk 1
# nama = {}
# nama['ayah'] = 'bambang'
# nama['ibu'] = 'anna'
# nama['anak1'] = 'Raihan'
# nama['anak2'] = 'Anin'
# nama['anak3'] = 'Aisyah'

# print(nama)
# print(nama['ibu'])
# print(nama['anak1'])

# atau bentuknya bisa seperti ini
# bentuk2
identitas = {'id':101,
        'identitas':['anji','tohpati','lukas'],
        'absen':12,
        'alamat':'semarang',
        'gender':'laki'
}

identitas2 = {'id':102,
        'identitas':'bitchy',
        'absen':13,
        'alamat':'solo',
        'gender':'perempuan'
}

identitas_list = {12:identitas, 13:identitas2}
# memasukan DICTIONARY kedalam list

print(f"Nama tengah : {identitas['identitas'][1]}") #mengakses list
# print(identitas['identitas'][1]) #mengakses list
# print(identitas['absen'])
# print(identitas['gender'])
# print(identitas.keys())
# print(identitas.values())
# print(identitas.items()) #keys dan value

# print(identitas_list[13]) #pemanggilan list
