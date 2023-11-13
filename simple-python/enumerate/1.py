"""
Eğer yazdığınız bir programda numaralandırmaya ilişkin işlemler yapmanız gerekiyorsa
Python’ın size sunduğu çok özel bir fonksiyondan yararlanabilirsiniz. Bu fonksiyonun adı enumerate().

"""

print(*enumerate("beteljesedes"))   

# Enumerate kelimesi İngilizcede ‘numaralamak, numaralandırmak’ gibi anlamlara gelir.


print("------------------------------")


for i in enumerate("beteljesedes"):
    print(i)



print("------------------------------")

for sıra, harf in enumerate("beteljesedes", 1): # beteljesedes'ten sonra gelen -1- parametresi numaralandırmanın kaçtan başlayacağını gösterir
    print(sıra, harf)

