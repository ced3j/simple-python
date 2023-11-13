# Verilen sayının basamak sayısını bulan program

number = 1035913
counter = 0

if number <= 9:
    counter = 1
    print(counter)
else:
    while number > 0:
        number //= 10
        counter += 1

print(counter)
