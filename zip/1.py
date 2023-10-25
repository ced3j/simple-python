# Diyelim ki elimizde şöyle iki farklı liste var:

a1 = ['a', 'b', 'c']
a2 = ['d', 'e', 'f']

# Eğer bu listelerin öğelerini birbirleriyle eşleştirmek istersek zip() fonksiyonundan yararlanabiliriz.
zip(a1, a2)




# Bir örnek: 

isimler = ['ahmet', 'mehmet', 'zeynep', 'ilker']
yaşlar = [25, 40, 35, 20]
for i, y in zip(isimler, yaşlar):
    print('isim: {} / yaş: {}'.format(i, y))




names = ["Derin", "Ahmet", "Mehmet"]
ages = [10, 20, 25]

for i, (name, age) in enumerate(zip(names, ages)):
    print(i, name, age)