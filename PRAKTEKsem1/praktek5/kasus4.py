# kamus
ipk = float(input("Masukan IPK :"))

#algoritma
if(ipk > 4.0):
    print("anda jenius")
if( 3.5 <= ipk < 4.0):
    print("Dengan pujian / Cumlaude")
elif( 3.0 <= ipk < 3.5):
    print("Sangat memuaskan / Very Good")
elif( 2.75 <= ipk < 3.0):
    print("Memuaskan / Good")
else:
    print("Kamu tidak lulus")