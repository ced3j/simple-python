# Verilen listeden elemanları tek tek alıp [1,2,3,4,5,6,7,8,9,10,11,12] biçiminde bir liste oluşturalım

list1 = [[1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12]]
list2 = []

for x in list1:
    for y in x:
        list2.append(y)

print(list2)


list3 = [y for x in list1 for y in x]
print(list3)
