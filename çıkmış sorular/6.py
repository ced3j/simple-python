# Belirli bir aralıktaki asal sayıları bulan program
# Örneğin 1 ile 45 arasındaki asal sayıları ekrana yazdır


for i in range(3, 46):
    bolundu = False
    for j in range(2, i):
        if i % j == 0:
            bolundu = True
    if bolundu == False:
        print(i)
