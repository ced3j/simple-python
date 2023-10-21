# 1) İsim ve Soy isimleri atadığınız listeden rastgele isim ve soy isimler seçerek isim oluşturan kodu yazınız


import random

isimler = ["Ahmet", "Mehmet", "Ayşe", "Selma", "Yusuf"]
soyisimler = ["Kara", "Beyaz", "Mor", "Ülker"]

isim = random.choice(isimler)
soyisim = random.choice(soyisimler)

print(f"Oluşturulan rastgele isim-soyisim: {isim} {soyisim}")
