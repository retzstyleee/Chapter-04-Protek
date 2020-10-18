jamAwal = 23
jamAkhir = 6
menitAwal = 50
menitAkhir = 0

deltaJam = (jamAwal - jamAkhir) * 60
deltaMenit = (menitAwal - menitAkhir) 
deltaTotal = (deltaJam + deltaMenit) // 60

harga1 = 200000
harga2 = 10000

bayar1 = (deltaTotal-12) * 10000
bayar2 = 200000

totalBayar = bayar1 + bayar2

print("Jadi, User harus membayar sebanyak ")
print(totalBayar)