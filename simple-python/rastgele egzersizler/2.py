# 1.py'daki sorunun farklı bir yöntemi


arr = [1, 2, 3, 4, 5, 6, 8, 9]

eksik_rakam = None  # Eksik rakamı depolamak için değişken

# Diziyi sıralayarak eksik rakamı tespit etme
for i in range(1, len(arr)):
    if arr[i] - arr[i - 1] != 1:
        eksik_rakam = arr[i - 1] + 1
        break

# Eğer eksik bir rakam bulunduysa, eksik rakamı ekle
if eksik_rakam is not None:
    arr.insert(i, eksik_rakam)

# Sonucu ekrana yazdır
print("Düzeltilmiş Dizi:", arr)
