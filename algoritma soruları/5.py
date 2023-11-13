# Klavyeden girilen 20 adet sayıdan çitlerin toplamının tek sayıların toplamına oranını bulunuz

cift = 0
tek = 0

for i in range(21):
    number = int(input("Please enter a num: "))
    if number % 2 == 0:
        cift += number
    else:
        tek += number


print(f"Çiftler: {cift}, tekler: {tek}, sonuç: {cift/tek}")
