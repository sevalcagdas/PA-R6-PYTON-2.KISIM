sayi= int(input("Lütfen bir sayı giriniz : "))
if sayi>1:

    for i in range (2,sayi):
        if (sayi% i) ==0:
            print ("Sayi asal değildir")
            break
    else :
        print("Sayi asaldır")
