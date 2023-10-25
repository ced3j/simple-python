# 1)  Verilen 2 sayı arasında kalan sayılardan oluşan bir liste oluştur


def createList(input1, input2):
    newList = []

    if input1 < input2:
        while input1 <= input2: 
            newList.append(input1)
            input1 += 1

    else:
        while input1 >= input2:
            newList.append(input2)
            input2 += 1

    return newList

input1 = int(input("Please enter input1: "))
input2 = int(input("Please enter input2: "))

resulting_list = createList(input1, input2)
print(resulting_list)