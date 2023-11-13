# Verilen listedeki çift rakamların karelerinden oluşan bir liste

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Bundan sonra artık sadece pratik yol ile devam edelim

list2 = [number**2 for number in numbers if number % 2 == 0]
print(list2)
