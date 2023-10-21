# Bir array'deki elemanların toplamını bulan program

arr = [10, 20, 30, 40, 100, 200, 300]
toplam = 0

for i in range(1, len(arr)):
    toplam += arr[i]

print(toplam)
