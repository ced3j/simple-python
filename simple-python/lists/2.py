# Verilen listede "20" sayısı mevcutsa o sayının indexini bul ve 20yi 200 ile değiştir ve bunu sadece tek bir 20 için yap
# Listenin ilk 20 değeri için yap

list1 = [5, 10, 15, 20, 25, 50, 20]

index = list1.index(20)

list1[index] = 200
print(list1)
