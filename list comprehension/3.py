# Verilen listedeki çift rakamlardan bir liste oluştur

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = []

for number in numbers:
    if number % 2 == 0:
        list2.append(number)

print(list2)


# Pratik yol
list3 = [number for number in numbers if number % 2 == 0]
print(list3)
