yakit  = float(input("Aracınız kilometrede kaç Litre yakıyor :"))
yol = float(input("Alınan yol (km) :"))
benzin= 8

yakilan= yol*yakit
sonuc = float((yol * yakit)*benzin)
print("===============================")
print("Yakılan yakıt : {}\nAlınan yol : {}\nLitre Fiyatı : {}".format(yakilan,yol,benzin))
print("Yakıt Masrafların : {}".format(sonuc))
print("===============================")

