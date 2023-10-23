# verilen listedeki en büyük sayıyı bulan program

def largest(arr):
    maxNum = arr[0]

    for i in arr:
        if i >= maxNum:
            maxNum = i

    return maxNum


list = [10, 359, 19, 186]
print(largest(list))
