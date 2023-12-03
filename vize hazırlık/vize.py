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


def asalBul1():
    def asal_mi(sayi):
        if sayi < 2:
            return False
        elif sayi == 2:
            return True
        else:
            i = 2
            while i * i <= sayi:
                if sayi % i == 0:
                    return False
                i += 1
            return True

    print(asal_mi(3))
    print(asal_mi(11))
    print(asal_mi(14))


def asalBul2():
    # Sayının asal olup olmadığını kontrol et
    num = int(input("Bir sayı giriniz: "))
    asalMi = 0

    if num == 1:
        print(f"{num} sayısı asal değil")
        return

    for i in range(2, num):
        if num % i == 0:
            asalMi += 1
            break

    if asalMi == 0:
        print(num, " sayısı asaldır")
    else:
        print(num, " sayısı asal değil")


def asalBul3():

    def asalMi(sayi):

        if sayi == 1:
            return False
        if sayi == 2:
            return True

        for i in range(2, sayi):
            if sayi % i == 0:
                return False
                break
            else:
                return True
                break

    print(asalMi(63))


def faktoriyel():
    def fakHesapla(sayi):
        sonuc = 1
        while sayi > 1:
            sonuc *= sayi
            sayi -= 1
        return sonuc

    print(fakHesapla(5))


def factorial():
    sayi = int(input("Bir sayı giriniz= "))
    fact = 1

    for i in range(sayi, 1, -1):
        fact *= i

    print(f"Sonuç: {fact}")


def fibonacci():
    def fib(n):
        a, b = 0, 1
        while n > 0:
            print(a, end=" ")
            a, b = b, a + b
            n -= 1
    fib(8)


def tek_cift_sayi():
    def fonk(liste):
        tekler = []
        ciftler = []

        for sayi in liste:
            if sayi % 2 == 0:
                ciftler.append(sayi)
            else:
                tekler.append(sayi)
        return tekler, ciftler

    num_list = [1, 2, 4, 10, 24, 155, 6, 8, 92]

    print(fonk(num_list))


def ebob1():
    def ebob_bul(a, b):
        while b:
            a, b = b, a % b
        return a

    print(ebob_bul(24, 36))


def ekok1():
    def ekok_bul(sayi1, sayi2):
        buyukSayi = sayi1
        if sayi1 > sayi2:
            buyukSayi = sayi1
        else:
            buyukSayi = sayi2

        ekok = buyukSayi
        while True:
            if ekok % sayi1 == 0 and ekok % sayi2 == 0:
                break
            ekok += buyukSayi

        return ekok

    print(ekok_bul(24, 32))


def ebob2():
    sayi1 = int(input("1. Sayıyı giriniz: "))
    sayi2 = int(input("2. Sayıyı giriniz: "))
    min = (sayi1 if sayi1 < sayi2 else sayi2)

    ebob = 0
    for i in range(1, min+1):
        if sayi1 % i == 0 and sayi2 % i == 0:
            ebob = i

    print(f"{sayi1} ve {sayi2} ebob'u: {ebob}")


def ekok2():
    sayi1 = int(input("1. Sayıyı giriniz: "))
    sayi2 = int(input("2. Sayıyı giriniz: "))
    max = sayi1*sayi2
    ekok = 0

    for i in range(max, 0, -1):  # Tersten
        if i % sayi1 == 0 and i % sayi2 == 0:
            ekok = i

    print(ekok)


# Tek bir sayı için çarpım tablosu
def carpimTablosuTek():
    def fonk(sayi):
        i = 1
        while i <= 10:
            sonuc = sayi * i
            print(f"{sayi} x {i} = {sonuc}")

            i += 1

    fonk(5)


# Tüm çarpım tablosu
def carpimTablosu():
    i = 1
    while i <= 10:
        j = 1
        while j <= 10:
            print(f"{i} x {j} = {j*i}")
            j += 1
        print()
        i += 1


def kalanliBolme():
    def fonk(x, y):
        if x == y:
            print("İki sayı birbirine eşit olamaz")
        elif x == 0 or y == 0:
            print("Sayılar sıfıra eşit olamaz")
        else:
            while x > 0 or y > 0:
                if x == 0:
                    print(f"x: {x} y: {y}")
                    break
                elif y == 0:
                    print(f"x: {x} y: {y}")
                    break
                else:
                    if x > y:
                        print("x ", x)
                        x = x % y
                    else:
                        print("y ", y)
                        y = y % x

    fonk(9, 12)


# Sıralı arama algoritması
def lineer_search():
    def func(arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1

    my_arr = [10, 2, 5, 16, 8, 99, 27]
    target_value = 16
    result = func(my_arr, target_value)

    if result == -1:
        print("Aranılan değer bu listede mevcut değil")
    else:
        print(f"""
        
            Aradığınız değer =  {target_value}
            Bu listenin      =  {my_arr}
            {result}. index'inde mevcut
              
              """)


def binary_search():
    def func(arr, target):
        low, high = 0, len(arr)-1
        while low <= high:
            mid = (low+high)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return -1

    sorted_list = [1, 3, 4, 6, 7, 9, 14]
    result = func(sorted_list, 9)
    print(result)


def details():

    print("abc" * 3)

    print("Num: " + 42)  # hata verir
    # Olması gereken: print("Num: ", 42) ya da print("Num: " + str(42))

    result = "Py" + 3.6  # ifadesi hatalıdır olması gereken str(3.6)

    result2 = "Hello" + True  # string ile bool toplanır mı? Hayır hata verir


def bolenBul1():

    def bolenleri_bul(sayi):
        bolenler = []
        for i in range(1, sayi + 1):
            if sayi % i == 0:
                bolenler.append(i)
        return bolenler

    sayi = int(input("Bir sayı girin: "))

    bolenler = bolenleri_bul(sayi)

    print(f"{sayi} sayısının bölenleri: {bolenler}")


def bolenBul2():

    def bolenleri_bul(sayi):
        bolenler = [i for i in range(1, sayi + 1) if sayi % i == 0]
        return bolenler

    sayi = int(input("Bir sayı girin: "))
    bolenler = bolenleri_bul(sayi)

    print(f"{sayi} sayısının bölenleri: {bolenler}")


# recursive
def firstR():

    def factorial(n):
        # Temel durum: 0! ve !! = 1

        if n == 0 or n == 1:
            return 1
        else:
            # recursive adım: n! = n * (n-1)!
            return n * factorial(n-1)

    result = factorial(5)
    print(f"5! = {result}")


# recursive
def secondR():

    a = 5

    def fibonacci(n):
        # temel durum: n 0 veya 1 ise sonuç 1
        if n <= 1:
            return 1
        else:
            # Recursive adım
            # fib(n) = fib(n-1) * fib(n-2)

            return fibonacci(n-1) + fibonacci(n-2)

    result = fibonacci(a)
    print(f"Fibonacci({a}) = {result}")


# recursive
def thirdR():

    def azalt(s):
        if len(s) < 1:
            return s
        else:
            print(s)
            return azalt(s[1:])

    print(azalt('ispandinavya'))


# girilen 2 sayı arasındaki tek sayıları yazdıran program
def tekSayilar():

    firstNum = int(input("Please enter a num: "))
    secondNum = int(input("Please enter a num: "))

    while firstNum < secondNum:
        if (firstNum % 2 == 1):
            print(firstNum)

        firstNum += 1


# Girilen sayının mutlak değerini verir
def mutlakDeger():

    num = int(input("Mutlak değerini görmek istediğiniz sayı: "))

    if num >= 0:
        print(f"Girdiğiniz sayının mutlak değeri: |{num}|")
    else:
        print(f"Girdiğiniz sayının mutlak değeri: {num*(-1)}")


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

    print(f"Toplam = {toplam}")


def soru1():
    a = 10
    b = "5"
    c = a + int(b)
    d = str(a) + b
    e = int(str(a) + b)

    print("c: ", c)
    print("d: ", d)
    print("e: ", e)


def sequential_algorithm():
    def search(lst, target_value):
        # If the list is empty:
        if not lst:
            print("Search failed: The list is empty")
        else:
            # Select the first entry in the list as TestEntry
            test_entry = lst[0]

            # While the TargetValue is greater than TestEntry and there are still entries in the list:
            i = 1
            while i < len(lst) and target_value != test_entry:
                # Select the next entry in the list as TestEntry
                test_entry = lst[i]
                i += 1

            # If the TargetValue is equal to TestEntry:
            if target_value == test_entry:
                print("Search success: Target value found in the list")
            else:
                # Declare the search as a failure
                print("Search failed: Target value not found in the list")

    # Example usage:
    my_list = [1, 3, 5, 7, 9]
    search(my_list, 5)
    search(my_list, 6)


def ebob():
    sayi1 = 24
    sayi2 = 32
    min = 0
    ebob = 0

    if sayi1 > sayi2:
        min = sayi2
    else:
        min = sayi1

    for i in range(1, min):
        if sayi1 % i == 0 and sayi2 % i == 0:
            ebob = i

    print(ebob)


def girilenSayilariTopla():
    toplam = 0
    while True:
        user_input = input("Bir sayı giriniz, çıkmak için Q : ")
        if user_input == "q" or user_input == "Q":
            print("Çıkış yapılıyor...")
            break
        else:
            if user_input.isdigit():
                toplam += int(user_input)
            else:
                print("Lütfen sadece sayı giriniz...!")
                break

    print(toplam)


# enKucukSayi()
# enBuyukSayi()
# asalBul1()
# asalBul2()
# asalBul3()
# faktoriyel()
# factorial()
# fibonacci()
# tek_cift_sayi()
# ebob1()
# ekok1()
# ebob2()
# ekok2()
# carpimTablosuTek()
# carpimTablosu()
# kalanliBolme()
# lineer_search()
# binary_search()
# details()
# bolenBul1()
# bolenBul2()
# firstR()
# secondR()
# thirdR()
# tekSayilar()
# mutlakDeger()
# kdvOran()
# girilenSayiToplam()
# soru1()
# ebob()
# girilenSayilariTopla()

# sayi1 = 32
# sayi2 = 24
# min = sayi1 if sayi1 < sayi2 else sayi2
# ebob = 0
#
# for i in range(1, min):
#     if sayi1 % i == 0 and sayi2 % i == 0:
#         ebob = i
#
# sayi1K = sayi1 / ebob
# sayi2K = sayi2 / ebob
# sonuc = ebob * sayi1K * sayi2K
# print(sonuc)


def recurs(param1, param2):
    if param2 == 1:
        return param1
    return param1 * recurs(param1, param2-1)


print(recurs(2, 3))
