# Belirli bir aralıktaki asal sayıları bulan program

# 2, asal sayıların en küçüğüdür ve döngüye dahil edilmedi, bu nedenle manuel olarak ekleyebiliriz.
print(2)

# 3 ile 45 arasındaki asal sayıları bulmak için bir döngü kullanıyoruz.
for i in range(3, 46):
    bolundu = False

    # Asal sayıları kontrol etmek için bir iç içe döngü kullanıyoruz.
    for j in range(2, i):
        if i % j == 0:
            bolundu = True
            break  # İç içe döngüden çıkış yapılır.

    # Eğer i, iç içe döngüden hiçbir sayıya bölünmeden çıkarsa, o bir asal sayıdır ve ekrana yazdırılır.
    if bolundu == False:
        print(i)
