# Girilen bir sayının çarpım tablosunu yazdırın

num = int(input("Sayı giriniz: "))

for i in range(1, 11):
    print("{} x {} = {}". format(i, num, i*num))
