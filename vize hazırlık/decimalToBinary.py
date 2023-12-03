def decToBin(sayi):
    if sayi == 0:
        return "0b0"

    binary = ""
    while sayi > 0:
        binary = str(sayi % 2) + binary
        sayi //= 2
    return "0b" + binary


# Kullanıcıdan onluk tabandaki bir sayı alalım
onluk_sayi = int(input("Onluk tabandaki bir sayı girin: "))

# İkilik tabana çevirelim
ikili_sayi = decToBin(onluk_sayi)

# Sonucu ekrana yazdıralım
print(f"{onluk_sayi} sayısı ikili tabanda: {ikili_sayi}")


# ikili_sayi = bin(10)[2:]
# print(f"10 sayısı ikili tabanda: {ikili_sayi}")
