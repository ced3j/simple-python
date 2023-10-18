# Klavyeden kullanıcının girdiği 3 adet integer türünde ki sayıyı büyükten küçüğe sıralayarak ortadaki
# sayı ile büyük olan sayının arasındaki farkı ve yine ortadaki sayı ile küçük olan sayı ile arasındaki farkı ekrana yazdıran python kodlarını yazınız?

inputs = []

k = 0  # küçük
b = 0  # büyük
o = 0  # orta

while True:
    user_input = input("Değer eklemek için bir girdi girin: ")
    inputs.append(user_input)
    if (len(inputs) == 3):
        inputs.sort()
        break

print(inputs)

k = int(inputs[0])
b = int(inputs[2])
o = int(inputs[1])


print(f"Büyük - Ortanca: {b-o} Ortanca - Küçük: {o-k}")
