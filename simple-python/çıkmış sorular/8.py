# Kullanıcıdan 5 sayı iste, bunların ortalamasını hesapla ve ortalamaya en yakın sayıyı(5 sayı içinden) ekrana yazdır
# ( Daha düzgün çözüm versiyonu )

sayilar = []
toplam = 0

# Kullanıcıdan 5 adet sayı girişi al ve bunları 'sayilar' listesine ekle.
for _ in range(5):
    sayi = int(input("Sayı gir: "))
    sayilar.append(sayi)
    toplam += sayi

# 5 sayının ortalamasını hesapla.
ortalama = toplam / 5

# Sayıları küçükten büyüğe sırala.
sayilar.sort()

# Ortalamaya en yakın sayıyı bul.
en_yakin_sayi = sayilar[0]
for sayi in sayilar:
    if abs(ortalama - sayi) < abs(ortalama - en_yakin_sayi):
        en_yakin_sayi = sayi

# Sonuçları ekrana yazdır.
print("Sayılar:", sayilar)
print("Ortalama:", ortalama)
print("Ortalama en yakın sayı:", en_yakin_sayi)
