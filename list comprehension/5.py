# Verilen listedeki 4 ten büyük çift sayıların karelerinden oluşan bir liste
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list2 = [number**2 for number in numbers if number % 2 == 0 and number > 4]
print(list2)
