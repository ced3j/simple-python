# İki sayının toplamını hesaplama algoritması kullanıcı girdileriyle

# İlk olarak, kullanıcıdan num1 ve num2 adlı iki sayıyı girmesini istiyoruz.
# 'int(input(...))' kullanarak kullanıcıdan girdi alırken bu girdileri tam sayıya dönüştürüyoruz.

num1 = int(input("num1 değerini girin: "))
num2 = int(input("num2 değerini girin: "))


# Şimdi, kullanıcının girdiği iki sayının toplamını hesaplayıp sonucu 'sum' adlı bir değişkene kaydediyoruz.
sum = num1 + num2

# Sonucu ekrana yazdırmak için 'print' fonksiyonunu kullanıyoruz. 
# Burada, 'format' metodu kullanılarak ekrana toplam sonucu yazdırılıyor.
# 'format' metodu, kullanıcı girdilerini ve toplam sonucunu düzgün bir şekilde yerleştirir.
print('Toplam: {0} ve {1} = {2}'.format(num1, num2, sum))
