# 12 basamaklı ilk fibonacci sayısını ekrana yazdır

fibList = []
fibList.append(1)
fibList.append(1)
index = 2

while True:
    fibList.append(fibList[index-2] + fibList[index-1])

    terim = fibList[index-2] + fibList[index-1]

    if len(str(terim)) == 12:
        print(terim)
        break
    index += 1
