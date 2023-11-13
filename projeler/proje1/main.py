# listelerin, sözlüklerin,


list_methods = []
# dir: içine bir sınıf yazıldığında o sınıfın fonksiyonlarını liste olarak döndürür

for method in dir(list):
    if method.startswith("__"):  # __ ile başlayanlar özel fonksiyonlardır
        continue  # bunları görmek istemiyoruz
    list_methods.append(method)


set_methods = []  # kümeler yani set methodları

for method in dir(set):
    if method.startswith("__"):
        continue
    set_methods.append(method)


tuple_methods = []  # demet methodları yani tuples

for method in dir(tuple):
    if method.startswith("__"):
        continue
    tuple_methods.append(method)


string_methods = []  # string methodları

for method in dir(str):
    if method.startswith("__"):
        continue
    string_methods.append(method)


dict_methods = []  # sözlük/dictionary methodları

for method in dir(dict):
    if method.startswith("__"):
        continue
    dict_methods.append(method)


basliklar = ["List Methods", "Set Methods",
             "Tuple Methods", "String Methods", "Dict Methods"]


classes = [list_methods, set_methods,
           tuple_methods, string_methods, dict_methods]


# Burada en fazla methodu olan hangisiyse onu belirledik çünkü
# diğerlerinde boş kalan yerler olacak buralara ---- gibi çizgiler koymamız gerek

max_len = 0
for class_ in classes:
    if len(class_) > max_len:
        max_len = len(class_)


for baslik in basliklar:
    print(baslik, end="")
    print(" " * (30 - len(baslik)), end="")

# 30 karakterlik bir sütun genişliği ayarlayalım
for i in range(max_len):  # 0'dan max_len'e kadar dönecek
    print()  # her i değiştiğinde bir alt satıra geçilsin
    for class_ in classes:
        if i >= len(class_):  # Diyelim ki bizim demetlerimizde 2 tane method var fakat i == 3 olmuş yani bunun bir karşılığı yok
            # o yüzden buraya bir method ismi yazmaktansa boş çizgi çekelim
            # 7 tane çizgi ---  end ile alt satıra geçmeyi engelliyoruz boşluk yapmasını sağlıyoruz
            print("-------", end="")
            # 23 adet de boşluk karakteri toplamda 30luk bir sütun oldu
            print(" "*23, end="")
        else:
            print(class_[i], end="")
            # 30 karakterin kalan kısmını bu şekilde dolduralım
            print(" " * (30 - len(class_[i])), end="")
