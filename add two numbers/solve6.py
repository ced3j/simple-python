# Özyinelemeli (recursive) bir fonksiyon kullanarak iki sayının toplamını hesaplama algoritması
# recursive fonksiyon: kendi içinde kendini yeniden çağıran fonksiyonlardır diyebiliriz

# İlk olarak, 'add_numbers_recursive' adlı özyinelemeli bir fonksiyon tanımlıyoruz.
# Bu fonksiyon, x ve y adlı iki parametre alır.
def add_numbers_recursive(x, y):
    if y == 0:
        return x
    else:
        return add_numbers_recursive(x + 1, y - 1)

# Şimdi, num1 ve num2 adlı iki sayıyı saklıyoruz.
num1 = 1
num2 = 2

# Özyinelemeli fonksiyonu kullanarak, num1 ve num2'nin toplamını hesaplıyoruz.
result = add_numbers_recursive(num1, num2)

# Sonucu ekrana yazdırmak için 'print' fonksiyonunu kullanıyoruz. 
# Sonucu kullanıcı dostu bir şekilde görüntülemek için metin içinde değerleri yerleştiriyoruz.
print("Toplamı", num1, "ve", num2, "ise", result)
