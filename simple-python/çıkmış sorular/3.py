# Kullanıcının girdiği 3 tam sayıyı büyükten küçüğe sıralayarak ortadaki sayı ile farkları hesaplama algoritması

inputs = []

k = 0  # küçük
b = 0  # büyük
o = 0  # orta

# Kullanıcıdan 3 tam sayı girmesini istiyoruz ve bu girdileri bir diziye ekliyoruz.
while True:
    user_input = input("Değer eklemek için bir girdi girin: ")
    inputs.append(user_input)
    if (len(inputs) == 3):
        inputs.sort()  # Girdileri küçükten büyüğe sıralıyoruz.
        break

# Sıralanmış girdileri kullanarak küçük, orta ve büyük sayıları belirliyoruz.
k = int(inputs[0])
b = int(inputs[2])
o = int(inputs[1])

# Ortanca sayı ile büyük olan sayı arasındaki farkı ve ortanca sayı ile küçük olan sayı arasındaki farkı hesaplıyoruz.
fark1 = b - o
fark2 = o - k

# Farkları ekrana yazdırıyoruz.
print(f"Büyük - Ortanca: {fark1} Ortanca - Küçük: {fark2}")
