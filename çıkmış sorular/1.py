# 1
# Kullanıcın girdiği 5 basamaklı bir sayının, basamaklarının toplamını ekrana yazdıran python kodlarını yazınız?

num = input("5 basamaklı bir sayı giriniz: ")
toplam = 0

if len(num) != 5:
    print("Lütfen 5 basamaklı bir sayı giriniz!")
else:
    for i in range(len(num)):
        toplam += int(num[i])

print(toplam)
