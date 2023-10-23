# Girilen bir sayının kaç basamaklı olduğunu hesaplayan program

num = int(input("Bir sayı girin: "))
a = num

count = 0
while num != 0:
    num = num // 10
    count += 1

print("{} sayısının basamak sayısı: {}".format(a, count))
