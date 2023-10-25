# 3) Verilen bir listenin en başındaki eleman ile en sonundaki elemanı değiştir


def swapList(newList):
     
    newList[0], newList[-1] = newList[-1], newList[0]
 
    return newList
     

newList = [12, 35, 9, 56, 24]
print(swapList(newList))