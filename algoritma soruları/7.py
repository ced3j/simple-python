# 3 basamaklı sayıların kaç tanesi rakamlarının küplerinin toplamına eşittir?
sayac = 0

for i in range(100, 1000):
    i_str = str(i)  # Sayıyı bir stringe çevir

    kToplam = 0

    for a in i_str:
        a = int(a)  # Her karakteri tekrar bir tam sayıya çevir
        kToplam += a * a * a

    if i == kToplam:  # sayının kendisi ile rakamları küpleri toplamı eşitse
        print(i)
        sayac += 1

print("Toplam", sayac, "sayı bulundu.")


"""

liste = []

for sayi in range(100, 1000):
    toplam = 0
    gecici_sayi = sayi  # geçici sayı üzerinde işlem yapacağız sayıyı deforme etmemiz gerektiği için

    while gecici_sayi != 0: # sayının 0'a eşit olmaması için
        basamak = gecici_sayi % 10 # sayının her bir basamağını alıyoruz (10 ile bölümden kalan)
        toplam += basamak ** 3 # basamağın küpünü aldık
        gecici_sayi //= 10 # son basamağı sildik

    if toplam == sayi:
        liste.append(sayi)

print(liste)

"""
