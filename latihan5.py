import math
l = int(input("Jumlah mahasiswa laki-laki : "))
p = int(input("Jumlah mahasiswa perempuan : "))
JUmlahL = "*"*math.ceil(l/10)
jumlahP = "*"*math.ceil(p/10)
print("Laki-laki : " + JUmlahL + "("+str(l)+")")
print("Perempuan : " + jumlahP + "("+str(p)+")")