# Bir listenin tersi değerlerini başka bir listeye aktaralım

list1 = [101, 124, 35, 316, 177, 193]
list2 = []

for x in range(len(list1)-1, -1, -1):
    list2.append(list1[x])


print(list2)
