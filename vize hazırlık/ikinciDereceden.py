def ikinci_dereceden_kokler(a, b, c):
    # Diskriminantı hesapla
    delta = b**2 - 4*a*c

    # Diskriminantın işareti kontrol et
    if delta > 0:
        # İki gerçek kök var
        kok1 = (-b + (delta**0.5)) / (2*a)
        kok2 = (-b - (delta**0.5)) / (2*a)
        return kok1, kok2
    elif delta == 0:
        # İki kök eşit ve gerçek
        kok = -b / (2*a)
        return kok,
    else:
        # İki karmaşık kök var
        gercekKisim = -b / (2*a)
        karmaşıkKisim = (abs(delta)**0.5) / (2*a)
        kok1 = complex(gercekKisim, karmaşıkKisim)
        kok2 = complex(gercekKisim, -karmaşıkKisim)
        return kok1, kok2


# Kullanıcıdan katsayıları alalım
a = float(input("a katsayısını girin: "))
b = float(input("b katsayısını girin: "))
c = float(input("c katsayısını girin: "))

# Kökleri bulalım
kokler = ikinci_dereceden_kokler(a, b, c)

# Sonucu ekrana yazdıralım
print(f"Denklemin kökleri: {kokler}")
