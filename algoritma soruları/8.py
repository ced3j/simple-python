# fibonacci sayı dizisi ilk iki terimi 1 olan ve sonraki her terimi kendisinden önceki 2 terimin
# toplamı olan bir sayı dizisidir. ilk 100 fibonacci sayısını ekrana yazdırın
# 1,1,2,3,5,8,13,21...


fibonacciList = []
fibonacciList.append(1)
fibonacciList.append(1)


index = 2  # elimizde 0. ve 1. index zaten mevcut o yüzden 2den başlayalım
while True:
    fibonacciList.append(fibonacciList[index-2] + fibonacciList[index-1])
    index += 1

    if len(fibonacciList) == 20:
        break

print(fibonacciList)


"""
for ile yapılmış versiyonu:

for i in range(2, 100):
    fibonacciList.append(fibonacciList[i-2] + fibonacciList[i-1])


print(fibonacciList)

"""
