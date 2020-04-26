print("Mükemmel Sayı bulma makinesine hoşgeldin!")

def mukemmel(sayi) :
	toplam = 0
	for i in range(1,sayi) : 
		if (sayi %i == 0):
			toplam +=i
	return toplam == sayi

sayi = int(input("Sayı giriniz :"))
for i in range(1,sayi) :
	if (mukemmel(i)) :
		print("Mükemmel Sayı : ", i) 




