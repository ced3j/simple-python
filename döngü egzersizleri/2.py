# Adınızı girdiğiniz sayı kadar yazdıran program

name = input("Adınızı girin: ")
num = int(input("Kaç kez yazdırılsın? "))

for i in range(1, num+1):
    print(name)


print("---------------------------------------")
# 1'den 100'e kadar olan çift sayıları yazdır

for i in range(1, 101):
    if i % 2 == 0:
        print(i)
