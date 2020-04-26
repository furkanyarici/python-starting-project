print("En Büyük Ortak Bölen ( EBOB ) bulma makinesine hoşgeldin!")

def ebob_bul(sayi1,sayi2) : 
	i = 1
	ebob = 1
	while (i <= sayi1 and i <= sayi2) :
		
		if not (sayi1 % i) and not (sayi2 % i):
			ebob = i
		i+=1
	return ebob

sayi1 = int(input("Lütfen birinci sayıyı gir :"))
sayi2 = int(input("Lütfen ikinci sayıyı gir : "))

print("EBOB = ",ebob_bul(sayi1,sayi2))
	

