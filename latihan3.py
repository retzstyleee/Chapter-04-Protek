import math
jarak = 795
bensin = 1
jauh = 12
totalBensin = (jarak / (bensin*jauh))

print ("Jadi, bensin yang digunakan sebanyak")
print (totalBensin)

kapasitas = 50
banyakPengisian = math.ceil(totalBensin/kapasitas)
print ("dan memerlukan sebanyak " +str(banyakPengisian) + "x pengisian ulang")
