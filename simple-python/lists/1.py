# Bir listeyi tersine çevir

list1 = [100, 200, 300, 400, 500]
list1.reverse()
print("List1: ",list1)

print("--------------------------------------------")

list2 = [10, 20, 30, 40, 50]
list2 = list2[::-1]
print("List2: ", list2)

print("--------------------------------------------")


# İki listeyi birleştir

listA = ["M", "na", "i", "Ke"]
listB = ["y", "me", "s", "lly"]
listC = [i + j for i, j in zip(listA, listB)]

print(listC)

