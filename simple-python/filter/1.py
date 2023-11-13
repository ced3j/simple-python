"""
Bu gömülü fonksiyon yardımıyla dizi niteliği taşıyan nesneler içindeki öğeler üzerinde belirli 
bir ölçüte göre bir süzme işlemi uygulayabiliriz. Dilerseniz filter() fonksiyonunun 
görevini bir örnek üzerinden anlamaya çalışalım.

"""

liste = [400, 176, 64, 175, 355, 13, 207, 298, 397, 386, 31, 120, 120, 236, 241, 123, 249, 364, 292, 153]

for i in liste:
    if i % 2 == 1:  # Eğer listenin i. elemanı'nın 2ye bölümünden kalan 1 ise i. elemanı yazdır
        print(i)

# [i for i in liste if i % 2 == 1]


""" İşte Python, yukarıdaki işlemi yapabilmemiz için bize üçüncü bir yol daha sunar. Bu üçüncü yolun adı filter() fonksiyonudur."""


def tek(sayı):
    return sayı % 2 == 1

print(*filter(tek, liste))

# tek adlı fonksiyon liste adlı listenin üzerinde uygulanıyor

# yani --> [i for i in filter(tek, liste)] -----> [i for i in liste if i % 2 == 1]
