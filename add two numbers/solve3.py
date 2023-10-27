# İki sayının toplamını hesaplamak için bir işlev (fonksiyon) tanımlama algoritması

# İki sayının toplamını hesaplayan bir işlev (fonksiyon) tanımlıyoruz.
# Bu işlev, a ve b adlı iki parametre alır ve bu parametrelerin toplamını döndürür.
def sumFunc(a, b):
    return a + b

# Kullanıcıdan num1 ve num2 adlı iki sayıyı girmesini istiyoruz.
# Bu girdileri 'int(input(...))' kullanarak tam sayıya dönüştürüyoruz.
num1 = int(input("num1 değerini girin: "))
num2 = int(input("num2 değerini girin: "))

# Fonksiyonu kullanarak, kullanıcının girdiği iki sayının toplamını hesaplayıp sonucu alıyoruz.
result = sumFunc(num1, num2)

# Sonucu ekrana yazdırmak için 'print' fonksiyonunu kullanıyoruz. 
# Sonucu, kullanıcı dostu bir şekilde görüntülemek için f-strings kullanıyoruz.
print(f'{num1} ve {num2} toplamı = {result}')


