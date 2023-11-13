# Move Zeros adında bir leetcode sorusu
# Bu soruda bize bir liste veriliyor içerisinde 0lar ve farklı rakamlar içeren bir liste
# Mesela:  [0,1,5,17,0,3]    bu listedeki sıfırları listenin en sonuna almalıyız
# Çıktımız şu olmalı:  [1,3,5,17,0,0]

arr = [0,1,5,17,0,3]

arr.sort()
numOfZeros = 0

# while 0 in arr ifadesi, bir liste içinde belirli bir değerin (bu durumda 0'ın) bulunup bulunmadığını kontrol eder. 
# Eğer liste içinde 0 varsa, bu ifade True değerini döndürür. Eğer liste içinde 0 yoksa, False değerini döndürür.
# True değeri döndüğü müddetçe de döngü çalışacaktır

while 0 in arr:
    arr.remove(0)
    numOfZeros += 1

for i in range(numOfZeros):
    arr.append(0)


print(arr)