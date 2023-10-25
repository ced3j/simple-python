# 1) Verilen bir listenin en başındaki eleman ile en sonundaki elemanı değiştir

list = [10, 20, 30, 40, 50]
first = list[0]
last = list[-1]

list[0] = last
list[-1] = first

print(list)