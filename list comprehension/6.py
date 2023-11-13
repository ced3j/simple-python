numbers = [1, 2, 3, 4]
letters = "abcd"

# [(1,a), (1,b), (1,c), (2,a) ........ (4,d)] şeklinde ikililerden oluşan bir liste

# Önce standart yol
list2 = []
for number in numbers:
    for letter in letters:
        list2.append((number, letter))

print(list2)


# listeye tuple biçiminde ekleme yapacağız o yüzden (number, tuple)
list3 = [(number, letter) for number in numbers for letter in letters]
print(list3)
