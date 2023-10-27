# 2) İsim ve Soy isimleri atadığınız listeden rastgele isim ve soy isimler seçerek isim oluşturan kodu yazınız

import random

def isimOlusturucu():
    isimler = ["Gözde", "Metehan", "Selma", "Gökçe", "Yusuf", "Murat", "Hakan"]
    soyisimler = ["Yiğiter", "Yaz", "Kış", "Bahar", "Kaya", "Tesla", "Ülker"]

    # random.choices() fonksiyonunu kullanarak rastgele bir isim ve soyisim seçiyoruz.
    secilen_isim = random.choice(isimler)
    secilen_soyisim = random.choice(soyisimler)

    return f"{secilen_isim} {secilen_soyisim}"

# isimOlusturucu işlemini 10 kez tekrarlayarak 10 farklı rastgele isim oluşturuyoruz.
for i in range(10):
    print(isimOlusturucu())
