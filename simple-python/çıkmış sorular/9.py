# Kullanıcının girdiği sayılardan en büyük olanını bulan program

# Bir dizi (array) içindeki en büyük sayıyı bulan bir işlev (fonksiyon) tanımla.
def max_number(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

# Kullanıcıdan kaç adet sayı gireceğini sor.
size = int(input("Kaç adet sayı gireceksiniz?: "))

array = []  # Girilen sayıları saklamak için bir dizi oluştur.

# Kullanıcıdan sayıları giriş yapmasını iste ve diziyi doldur.
for i in range(size):
    array.append(int(input("{}. sayıyı gir: ".format(i+1))))

# Girilen sayıların en büyük olanını bul ve ekrana yazdır.
print("Girilen en büyük sayı:", max_number(array))
