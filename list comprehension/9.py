list_methods = []

for method in dir(list):
    if method.startswith("__"):
        continue
    list_methods.append(method)

print(list_methods)


# Şimdi de yukarıdaki kodu tek satıra düşürelim

list2 = [method for method in dir(list) if not method.startswith("__")]
print(list2)
