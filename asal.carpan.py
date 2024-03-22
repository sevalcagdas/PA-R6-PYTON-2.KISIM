def asal_carpanlari_bul(sayi):
    asal_carpanlar = []
    carpan = 2  # Asal çarpanları bulmak için başlangıç değeri

    while carpan * carpan <= sayi:
        if sayi % carpan == 0:
            asal_carpanlar.append(carpan)
            sayi //= carpan  # Sayıyı böldükçe küçült
        else:
            carpan += 1

    if sayi > 1:
        asal_carpanlar.append(sayi)

    return asal_carpanlar

sayi = int(input("Bir sayı girin: "))
asal_carpanlar = asal_carpanlari_bul(sayi)
print(f"{sayi} sayısının asal çarpanları: {asal_carpanlar}")