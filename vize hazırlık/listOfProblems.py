# Kullanıcıdan 3 sayı al en küçüğünü bul
def enKucukSayi():

    x = True
    numList = []

    while x:
        sayi = int(input("Bir sayı gir: "))
        numList.append(sayi)

        if len(numList) == 3:
            x = False

    enK = numList[0]
    for i in range(len(numList)):
        if numList[i] < enK:
            enK = numList[i]

    print(f"{numList} sayıları arasındaki en küçük sayı: {enK}")


def enBuyukSayi():
    s1 = int(input("1. sayı: "))
    s2 = int(input("2. sayı: "))
    s3 = int(input("3. sayı: "))
    max = s1

    if s1 > s2 and s1 > s3:
        max = s1
    elif s2 > s1 and s2 > s3:
        max = s2
    else:
        max = s3

    print(f"En büyük sayı: {max}")


def carpimTablosu():

    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}")


def tekCift():

    while True:
        sayi = int(input("Sayı giriniz: (Programdan çıkmak için 0 giriniz) --> "))

        if sayi == 0:
            break
        else:
            if sayi % 2 == 0:
                print(f"Girdiğiniz {sayi} sayısı çifttir.")
            else:
                print(f"Girdiğiniz {sayi} sayısı tektir.")


# 2 sayı arasındaki tek ve çift sayılar
def ikiAraliktaTekVeCift():
    for i in range(1, 100, 2):
        print(i, end=" ")
    print()

    for i in range(0, 101, 2):
        print(i, end=" ")

    print()

    for i in range(13, 100, 2):
        print(i, end=" ")

    print()

    num1 = int(input("1. sayıyı giriniz: "))
    num2 = int(input("2. sayıyı giriniz: "))

    for i in range(num1, num2+1, 2):
        print(i, end=" ")


# 2 sayı arasındaki tek ve çift sayılar çarpımı ve toplamı
def ikiAraliktaCarpimToplam():
    tekToplam = 0
    tekCarpim = 1

    ciftToplam = 0
    ciftCarpim = 1

    for i in range(1, 16):
        if i % 2 == 0:
            ciftToplam += i
            ciftCarpim *= i
        else:
            tekToplam += i
            tekCarpim *= i
    print(f""" 
        
        Tek sayıların toplamı: {tekToplam}
        Tek sayıların çarpımı: {tekCarpim}
        Cift sayıların toplamı: {ciftToplam}
        Cift sayıların çarpımı: {ciftCarpim}

        """)


def kdvOran():
    fiyat = int(input("Ürünün fiyatını giriniz: "))
    oran = float(input("KDV Oranı(%): "))

    yeniFiyat = fiyat + ((fiyat * oran)/100)
    print(f"KDV'li fiyat: {yeniFiyat}")


def girilenSayiToplam():

    toplam = 0

    while True:

        sayi = input("Sayı giriniz (Programdan çıkış için Q): ")
        if sayi == "q":
            break
        if sayi.isnumeric():
            toplam += int(sayi)

    print(toplam)


def ebob():
    sayi1 = int(input("1. Sayıyı giriniz: "))
    sayi2 = int(input("2. Sayıyı giriniz: "))
    min = (sayi1 if sayi1 < sayi2 else sayi2)

    ebob = 0
    for i in range(1, min+1):
        if sayi1 % i == 0 and sayi2 % i == 0:
            ebob = i

    print(f"{sayi1} ve {sayi2} ebob'u: {ebob}")


def ekok():
    sayi1 = int(input("1. Sayıyı giriniz: "))
    sayi2 = int(input("2. Sayıyı giriniz: "))
    max = sayi1*sayi2
    ekok = 0

    for i in range(max, 0, -1):  # Tersten
        if i % sayi1 == 0 and i % sayi2 == 0:
            ekok = i

    print(ekok)


def bolenler():
    for i in range(1, 12):
        if 12 % i == 0:
            print(i)


def asalSayi():

    def asalMi(sayi):

        if sayi == 1:
            return False
        if sayi == 2:
            return True

        for i in range(2, sayi):
            if sayi % i == 0:
                return False
            else:
                return True

    print(asalMi(3))


# Belirli bir aralıktaki asal sayı
def araliktakiAsalSayi():
    for i in range(2, 200):
        asal = True
        for j in range(2, i):
            if i % j == 0:
                asal = False
        if asal:  # True ise
            print(i, end=" ")


def factorial():
    sayi = int(input("Bir sayı giriniz= "))
    fact = 1

    for i in range(sayi, 1, -1):
        fact *= i

    print(f"Sonuç: {fact}")


# Bir sayının basamak değerlerinin faktöriyellerinin toplamı o sayıya eşitse
def factorion():

    def faktoriyel(sayi):
        f = 1
        for i in range(sayi, 1, -1):
            f *= i

        return f

    sayi = int(input("Sayı giriniz: "))
    toplam = 0
    temp = sayi
    while temp > 0:
        kalan = temp % 10
        toplam += faktoriyel(kalan)
        temp = temp // 10

    if sayi == toplam:
        print("Sayı faktöriyondur")

    else:
        print("Sayı faktöriyon değildir")


# enKucukSayi()
# enBuyukSayi()
# carpimTablosu()
# tekCift()
# ikiAraliktaTekVeCift()
# ikiAraliktaCarpimToplam()
# kdvOran()
# girilenSayiToplam()
ebob()
# ekok()
# bolenler()
# asalSayi()
# araliktakiAsalSayi()
# factorial()
# factorion()
