# List Comprehension --- > elimizde bulunan bir listeden bazı yöntemleri kullanarak yeni bir liste oluşturmak
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# verilen listedeki rakamlardan oluşan bir liste oluşturalım
list2 = []
for number in numbers:
    list2.append(number)

print(list2)


# Daha pratik yol:
list3 = [number for number in numbers]
# ilk number = listeye eklenecek olan eleman
# ikinci number numbers içinde dönecek olan değer
# yani for'dan sonrası ilk number'ın bulunduğu konum gibi düşünülebilir
print(list3)
