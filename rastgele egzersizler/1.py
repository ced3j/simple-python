# verilen bir array içerisindeki eksikliği fark edip düzelten program
# mesela:   [1,2,3,4,5,6,8,9]  buradaki eksik rakam "7" yi bulup düzeltmesini bekliyoruz


arr = [1, 2, 3, 4, 5, 6, 8, 9]

eksik_rakam = None  # Eksik rakamı depolamak için değişken

for i in range(1, len(arr)):
    fark = arr[i] - arr[i-1]

    if fark > 1:
        eksik_rakam = arr[i-1] + 1
        break


if eksik_rakam is not None:
    arr.insert(i, eksik_rakam)

# Sonucu ekrana yazdır
print("Düzeltilmiş Dizi:", arr)
