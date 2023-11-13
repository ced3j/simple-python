# İlk 10.000 asal sayının kaç tanesi 3 ile başlar ve 7 ile biter?

prime_list = list()  # Boş bir liste

prime_list.append(2)  # 2 bir asal sayıdır bunu manuel olarak ekliyoruz
sayi = 3

while True:
    prime = True
    # Minik bi optimizasyon --- Bu satırın açıklaması aşağıda
    for i in range(2, int(sayi ** 0.5)+1):  # normalde (2, sayi) ile de halledilebilir
        if sayi % i == 0:
            prime = False
            break  # For döngüsünü kırar, While'ı değil

    if prime:  # yukarıdaki if bloğuna girmemişse bu bloğa girecektir
        prime_list.append(sayi)  # Öyleyse sayı asaldır

        if len(prime_list) == 10000:
            break  # Eğer listenin eleman sayısı 10.000 olmuşsa while'dan çık

    sayi += 1  # sıradaki sayıya geçebilmek için sayıyı arttıralım


sonuc = []

for prime in prime_list:
    if str(prime).startswith("3") and str(prime).endswith("7"):
        sonuc.append(int(prime))

print(sonuc)
print(len(sonuc))


print(32 ** 0.5)


"""
for i in range(2, int(sayi ** 0.5)+1):

örneğin 100 sayısının asal olup olmadığını bulmak için

for i in range(2, 101):
burada 2 ile 100 arasındaki tüm sayılara bölünüp bölünmediğini deneyebiliriz fakat bu pek optimize bir yol değil
çok yorucu ve zaman alıcı

bundan daha mantıklı olan şudur:
2 ile 10 arasındaki sayılarla deneyip bölünüp bölünemediğine bakmak yeterli
Örneğin 50 sayısı 5*10 diyebiliriz
Biz burada 50 sayısının 25'e bölünüp bölünmediğine bakarak da asal olup olmadığını anlayabiliriz ama 5'te bölündüğü zaman daha erken anlarız 
Aynı şekilde 100 sayısı 10*10 burada ya da 5*20 ya da 4*25 ise örneğin, bu döngü 2 ile 100 arasında gidip gelmektense
4 rakamına geldiği an sayının asal olup olmadığını anlar ve sıradaki işleme geçer 
o yüzden sayı'nın 0.5 kuvvetini alıyoruz



"""
