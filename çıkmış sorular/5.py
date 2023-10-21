# 2) İsim ve Soy isimleri atadığınız listeden rastgele isim ve soy isimler seçerek isim oluşturan kodu yazınız

import random


def isimOlusturucu():
    isim = ["Gözde", "Metehan", "Selma", "Gökçe", "Yusuf", "Murat", "Hakan"]
    soyisim = ["Yiğiter", "Yaz", "Kış", "Bahar", "Kaya", "Tesla", "Ülker"]

    return "{} {}".format(random.choices(isim), random.choices(soyisim))


for i in range(10):
    print(isimOlusturucu())
