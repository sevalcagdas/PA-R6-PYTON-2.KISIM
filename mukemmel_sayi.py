dizi=[]
toplam=0
Mukemmel_sayi=int(input("bir sayı giriniz:"))
for i in range(1,Mukemmel_sayi):
    if Mukemmel_sayi%i==0:
        dizi.append(i)
        toplam+=i
if toplam==Mukemmel_sayi :
    print(f"bu sayı mükemme bir sayi bu =>{dizi} bölenlerin toplamı={toplam}")
else:
    print("girdiğin sayı mükemmel değil")