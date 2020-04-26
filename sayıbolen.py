def tambolenleribul(sayi) :
	tam_bolenler = []

	for i in range(2,sayi) :
		tam_bolenler.append(i)
	return tam_bolenler

while True :

	sayi = input("Sayı girin : ")
	if (sayi == "q") :
		print("Çıkış yapılıyor...")
		break
	else : 
		sayi = int(sayi)
		print("Tam bölenler :" , tambolenleribul(sayi))
