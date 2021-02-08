print("---------------kasus 1---------------")
#kamus
a = 1
b = 4
#algoritma
print("hasil a yang pertama: "+str(a))
print("hasil b yang pertama: "+str(b))
b = a 
a -= b
print("hasil a yang pertama: "+str(a))
print("hasil b yang pertama: "+str(b))
a = b + 1
b = a / b
print("hasil a yang pertama: "+str(a))
print("hasil b yang pertama: "+str(int(b)))

print("---------------kasus 2---------------")
x = 0
y = 1 
hasil = 2*x + y*5
print("jawaban untuk kasus 2 adalah",hasil) 

print("---------------kasus 3---------------")
a = 1.0
t = 3.0
hasil = 0.5*a*t
print("jawaban untuk kasus 3 adalah",hasil)

print("---------------kasus 4---------------")
vo = 0
t = 12.5 
vt = 21.55
# vt = vo + a*t  rumus asli
a = (vt - vo) / t
print(a)