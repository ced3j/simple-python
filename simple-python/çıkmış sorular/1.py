# Kullanıcının girdiği 5 basamaklı bir sayının basamaklarının toplamını hesaplama algoritması

# Kullanıcıdan 5 basamaklı bir sayı girmesini istiyoruz.
num = input("5 basamaklı bir sayı giriniz: ")
toplam = 0

# Girilen sayının uzunluğunu kontrol ediyoruz. Eğer 5 basamaklı değilse hata mesajı veriyoruz.
if len(num) != 5:
    print("Lütfen 5 basamaklı bir sayı giriniz!")
else:
    # Sayının her basamağını dolaşarak toplam değişkenine ekliyoruz.
    for i in range(len(num)):
        toplam += int(num[i])

# Toplamı ekrana yazdırıyoruz.
print(toplam)
