# 1) İsim ve Soy isimleri atadığınız listeden rastgele isim ve soy isimler seçerek isim oluşturan kodu yazınız


import random

isimler = ["Ahmet", "Mehmet", "Ayşe", "Selma", "Yusuf"]
soyisimler = ["Kara", "Beyaz", "Mor", "Ülker"]

# İsimler ve soyisimler listelerinden rastgele bir isim ve soyisim seçiyoruz.
isim = random.choice(isimler)
soyisim = random.choice(soyisimler)
# random.choice ile choice içerisine girilen parametreden rastgele bir seçim yaparız

# Oluşturulan rastgele isim ve soyisimi ekrana yazdırıyoruz.
print(f"Oluşturulan rastgele isim-soyisim: {isim} {soyisim}")
