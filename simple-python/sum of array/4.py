# Collections kütüphanesi kullanım

from collections import Counter

arr = [10, 23, 35, 19, 92]
x = Counter(arr)
toplam = 0

for key, value in x.items():
    toplam += key * value

print("{} array toplamı : {}".format(arr, toplam))
