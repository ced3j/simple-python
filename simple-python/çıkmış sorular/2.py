# 2
# Kullanıcın girdiği 5 basamaklı bir sayının, basamaklarının toplamını ekrana yazdıran python kodlarını yazınız?
num = input("5 basamaklı bir sayı giriniz: ")

if len(num) != 5:
    print("Geçerli bir 5 basamaklı sayı girmelisiniz...")
else:
    num = int(num)
    toplam = 0
    while num > 0:
        toplam += num % 10
        num //= 10

print(f'Girdiğiniz sayının basamakları toplamı = {toplam}')


# len(num) != 5    5 basamaklı olup olmadığını ölçer
# not num.isdigit()    girilen değerin rakamlardan oluşup oluşmadığını ölçer
# not num.isdigit() yani  eğer girdi rakamlardan oluşmuyorsa diye okunur
# num //= 10   sayının son basamağını atmak için kullanılır
