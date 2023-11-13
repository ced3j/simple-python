# Lambda fonksiyonu kullanarak iki sayının toplamını hesaplama algoritması

# İlk olarak, 'add_numbers' adlı bir lambda fonksiyonu tanımlıyoruz.
# Bu lambda fonksiyonu, x ve y adlı iki parametre alır ve bu parametrelerin toplamını döndürür.
add_numbers = lambda x, y: x + y

# Şimdi, num1 ve num2 adlı iki sayıyı saklıyoruz.
num1 = 10
num2 = 30

# Lambda fonksiyonunu kullanarak, num1 ve num2'nin toplamını hesaplıyoruz.
result = add_numbers(num1, num2)

# Sonucu ekrana yazdırmak için 'print' fonksiyonunu kullanıyoruz. 
# Sonucu, format kullanarak ekrana yazdırıyoruz.
print("Toplamı {0} ve {1} = {2}".format(num1, num2, result))
