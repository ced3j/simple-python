# 1. listede bulunup 2. listede bulunmayan rakamların karesinden oluşan bir liste

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [2, 3, 6, 9, 5]


list3 = []

for i in list1:
    if i not in list2:
        list3.append(i**2)

print(list3)


list4 = [number**2 for number in list1 if number not in list2]
print(list4)
