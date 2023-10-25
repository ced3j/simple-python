# Diyelim ki elimizde şöyle bir liste var:

liste = [2, 3, 4, 5, 6]

# Amacımız bu liste içindeki her öğenin karesini hesaplamak. Bunun için şöyle bir yol izleyebiliriz:

for i in liste:
    i ** 2

# Ama buna gerek yok.  Bu tür bir işlemi yapmanın bir başka yolu da map() adlı bir gömülü fonksiyondan yararlanmaktır


def kareAl(n):
    return n**2

# Burada bir n sayısının karesini alan bir fonksiyon tanımladık şimdi map() kullanarak bunu bir liste üzerine uygulayalım
x = list(map(kareAl, liste)) # "list" kullanarak dönüşüm yapmazsak bize sadece map objesi dönecektir
print(x)