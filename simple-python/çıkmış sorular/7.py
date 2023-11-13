# Kullanıcıdan 5 sayı iste, bunların ortalamasını hesapla ve ortalamaya en yakın sayıyı(5 sayı içinden) ekrana yazdır

sayilar = []
ortalama = 0

while True:
    sayi = int(input("Sayı gir: "))
    sayilar.append(sayi)

    if (len(sayilar) == 5):
        break


for i in sayilar:
    ortalama += i

ortalama /= 5

sayilar.append(ortalama)
sayilar.sort()


print(ortalama)
print(sayilar)
print(sayilar.index(ortalama))

if (abs(ortalama - sayilar.index(ortalama)+1) < abs(ortalama - sayilar.index(ortalama)-1)):
    print("Ortalamaya en yakın sayı: ", sayilar[sayilar.index(ortalama)+1])
elif (abs(ortalama - sayilar.index(ortalama)+1) > abs(ortalama - sayilar.index(ortalama)-1)):
    print("Ortalamaya en yakın sayı: ", sayilar[sayilar.index(ortalama)-1])
else:
    print("Ortalama sayı aynı anda 2 farklı sayıya eşit yakınlıkta çıktı!")
