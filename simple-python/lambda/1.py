denklem = lambda x: x*2
# lambda isimsiz fonksiyondur değişkenlere atanabilir
# burada x aşağıdan gönderilen 2yi temsil eder
# lambda x,y,z:  yazarak 3 farklı parametre de verebilirdik daha fazla parametre de verilebilirdi
# sağ taraf yani x*2 ise işlem kısmını temsil eder

print(denklem(2))


kare_al = lambda x: x*x
kup_al = lambda x: x*x*x

print(kup_al(5))


toplam = lambda x, y: x+y
print("Toplam: {0}".format(toplam(10, 20)))


toplam2 = lambda *args: sum(args)
print("Args ile toplam1: {}".format(toplam2(10, 20, 30, 40, 50)))
print("Args ile toplam2: {}".format(toplam2(10, 20, 30)))

# Burada *args --> kaç tane paramatre alınacağı belli olmayan durumlarda kullanılır
# sum ise toplama methodudur 



# lambda'yı bir değişkene atamadan kullanmak
print((lambda x,y,z: x*y+z)(3,5,6))
# lambda ifadesini baştan sona parantez içine alıp yanına yeni parantez açıyoruz (3,5,6) bunlar da x,y,z parametreleri




print((lambda *args: sum(args)/len(args))(3, 5, 6))
# 3, 5 ve 6'yı toplayıp ortalamayı bulacak
# sum ile args'ı toplayıp len(args) ile uzunluğa bölecek



liste = [("Ali", 20), ("Veli", 19), ("Emel", 30), ("Ahmet", 34)]
liste.sort() # sort kullanarak listedeki isimlerin harflerine göre sıralama yaptık

print(liste)

# Eğer isimlere göre değil de yaşlara göre sıralama yapmak istersek
# sort--> key adında bir parametre alır ve bu key bizden neyin sıralanacağını söylememizi ister, bunu bir fonksiyon ile ifade etmemiz gerekir
# burada da lambda fonksiyonu kullanabiliriz
# Örnek: 


liste.sort(key = lambda x: x[1])
# burada lambda x ---> her bir x ("Ali", 20) yani bir demeti temsil eder
# x[0] --> ("Ali")
# x[1] --> 20  
# Yani bizim x[1] lere göre sıralama yapmamız gerek 

print(liste)


