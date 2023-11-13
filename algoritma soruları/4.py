# Girilen 3 basamaklı bir sayının basamaklarının küpleri toplamı sayının
# kendine eşit olup olmadığını bulan program


while True:
    number = input("3 basamaklı bir sayı giriniz: ")
    firstNum = number

    if len(number) == 3 and number.isnumeric():
        number = int(number)
        toplam = 0

        for i in range(3):
            digit = number % 10  # get the last digit
            toplam += digit ** 3
            number //= 10  # Remove the last digit

        if toplam == int(number):
            print(f"""
                  Sayı kendisine eşittir
                  İlk sayı: {firstNum}
                  küpler toplam: {toplam}
                  """)
        else:
            print(f"""
                  Sayı kendisine eşit değildir
                  İlk sayı: {firstNum}
                  küpler toplam: {toplam}
                  """)
        break
    else:
        print("Girdiğiniz sayı 3 basamaklı bir tam sayı olmalıdır!")
