import operator

# operator.add() yöntemi kullanarak iki sayının toplamını hesaplama algoritması

# İlk olarak, iki sayıyı saklamak için num1 ve num2 adlı iki değişken oluşturuyoruz.
num1 = 10
num2 = 20

# 'operator.add()' yöntemini kullanarak num1 ve num2'nin toplamını hesaplıyoruz.
# Sonucu 'print' fonksiyonuyla ekrana yazdırıyoruz.
print("İki sayının toplamı : ", end="")
print(operator.add(num1, num2))
