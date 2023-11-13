# Verilen listedeki rakamların karelerinden oluşan bir liste
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = []

for number in numbers:
    list2.append(number**2)


print(list2)


# Daha pratik yol:
list3 = [number**2 for number in numbers]
print(list3)
