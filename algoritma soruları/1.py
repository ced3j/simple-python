# Çarpma işlemini toplama işlemi kullanarak gerçekleştiren program

print("Çıkış yapmak için Q yazın")
a = 1
while a:
    num1 = input("Sayı 1: ")
    num2 = input("Sayı 2: ")
    toplam = 0
    try: 
        if num1.lower() == "q" or num2.lower() == "q":
            print("Çıkış yapılıyor...")
            a = 0
            break
        num1 = int(num1)
        num2 = int(num2)
        for i in range(abs(num1)):
            toplam += abs(num2)
        if num1 < 0 or num2 < 0:
            toplam = -toplam
        print(f"Sonuç: {toplam}")
    except ValueError:
        print("Geçersiz bir sayı girdiniz.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        a = 0



"""
print("Çıkış yapmak için Q yazın"): Kullanıcıya çıkış yapmak için "Q" girebileceğini belirten bir başlangıç mesajı yazdırılır.

a = 1: Bu değişken, programın çalışmaya devam etmesini kontrol eder. Başlangıçta 1 olarak ayarlanır.

while a:: Bu while döngüsü, a değişkeni 1 olduğu sürece çalışır. Yani, kullanıcı çıkış yapana kadar veya bir hata oluşana kadar çalışmaya devam eder.

num1 = input("Sayı 1: ") ve num2 = input("Sayı 2: "): Kullanıcıdan iki sayı girmesini isteyen girdi komutlarıdır.

toplam = 0: İki sayının çarpım sonucunu tutacak bir değişkeni başlangıçta 0 olarak ayarlar.

if num1.lower() == "q" or num2.lower() == "q":: Kullanıcı "q" girdiyse, çıkış yapılır. .lower() metodu, kullanıcının büyük veya küçük harfle girmiş olabileceği durumları dikkate alır.

num1 = int(num1) ve num2 = int(num2): Kullanıcının girdiği sayıları tamsayıya dönüştürür.

for i in range(abs(num1)):: Bu döngü, num1'in mutlak değeri kadar çalışır. Yani, negatif sayılar için de işlem yapılmasını sağlar.

toplam += abs(num2): Döngü içinde, her adımda toplam değişkenine num2'yi ekler. Bu, çarpma işlemini toplama işlemi kullanarak simüle eder.

if num1 < 0 or num2 < 0:: Eğer num1 veya num2 negatifse, sonucu negatif yapmak için bu kontrol yapılır.

print(f"Sonuç: {toplam}"): Çarpma işleminin sonucunu ekranda görüntüler.

except ValueError:: Kullanıcı geçersiz bir sayı girdiğinde bu hata yakalanır ve kullanıcıya bir uyarı verilir.

except Exception as e:: Herhangi bir beklenmeyen hata durumunda program, hatayı yakalar ve kullanıcıya bir hata mesajı gönderir.

a = 0: Bir hata oluştuğunda veya kullanıcı çıkış yaptığında, a değişkeni 0 olarak ayarlanır ve döngü sona erer, program sonlanır.




"""