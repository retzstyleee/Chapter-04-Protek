import math
jarakAB = 125
jarakBC = 256
kecepatanAB = 62
kecepatanBC = 70
jamBerangkat = 6
istirahat = 3/4 #45menit
sampaiC = math.floor((jamBerangkat + (jarakAB/kecepatanAB) + (jarakBC/kecepatanBC) + istirahat)*60)
jamSampaiC = math.floor(sampaiC / 60)
menitSampaiC = sampaiC % 60
print ("Jadi Pak Amir sampai di kota C pada pukul " + str(jamSampaiC) + "." + str(menitSampaiC))