while True:
    x = input("Bir sayı girin(çıkmak için q) = ")

    if not x or x == "q":
        break # döngüyü tamamen durdurur
    try:
        y = float(x)

    except:
        print("Geçersiz input")
        continue # döngüyü en başa gönderir

    print(y**2)
