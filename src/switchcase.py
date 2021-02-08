def hari(i):
     switcher={
          0:'senin',
          1:'selasa',
          2:'rabu',
          3:'kamis'
     }
     return switcher.get(i, "tidak ada hari")
print(hari(2))


