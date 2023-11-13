try:
    a = 5
    b = 0

    if b == 0:  # Eğer b sıfıra eşitse ZeroDivisionError fırlat
        raise ZeroDivisionError

    c = a / b
    x = 4
    d = x
    isim = "Derin"
    karakter = isim[10]

except ZeroDivisionError as e:  # 0'a bölüm hatası
    print("Payda sıfır olmamalı")
    # ZeroDivisionError hatasına isimlendirme yaptık yani artık "e" bunu temsil ediyor
    print(e)
except NameError:
    print("Bu değişken daha önce tanımlanmamış")
except IndexError:
    print("Böyle bir index bulunmuyor")
except Exception:  # Yukarıdaki hatalara uymayan herhangi bir hatada burası çalışır
    # yani aslında if else yapısındaki else kısmı gibi
    print("Bilinmeyen bir hata oluştu")

else:
    print("Else bloğu çalışıyor")
