# Kullanıcının girdiği sayılardan en büyük olanı bulan program

def max_number(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]

    return max


size = int(input("Kaç adet sayı gireceksiniz?: "))

array = []
for i in range(size):
    array.append(int(input("{}. sayıyı gir: ".format(i+1))))

print("Girilen en büyük sayı:", max_number(array))
