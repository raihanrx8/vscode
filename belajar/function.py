def botol():
    print("Harga 1 botol Rp 5000")

def kardus():
    botol()
    print("Harga 1 kardus Rp 50000")
    # botol = 5000*x
    # print("Harga total botol : Rp", botol)

def paket(x):
    kardus()
    print("total pembelian untuk",x,"paket")
    botol = 5000
    total = botol*x
    print("harga",x ,"botol :", total) 



# kardus()
paket(2)


