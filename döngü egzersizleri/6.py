# Bazı döngü çeşitleri

for key, value in enumerate(['A', 'B', 'C', 'D']):
    print(key, value)


print("----------------------------")


names = ["Betel", "Jesedes", "Schol"]
ages = (25, 19, 29)

for name, age in zip(names, ages):
    print("name: ", name)
    print("age: ", age)
    print()


print("----------------------------")


king = {'Ashoka': 'The Great',
        'Chandragupta': 'The Maurya', 'Modi': 'The Changer'}

for key, value in king.items():
    print(key, value)


print("----------------------------")
# Verilen listeyi tersine çevirip yazdır

liste = [1, 15, 61, 35, 16, 11135, 37]
for i in reversed(liste):
    print(i, end=" ")


print()
print("----------------------------")
# -10 ile 0 arasındaki sayıları 1er 1er say    --- anlamına gelir
for num in range(-10, 0, 1):
    print(num)


print("----------------------------")
# azalan tarzda döngüler

for i in range(6, 0, -1):
    print(i)
