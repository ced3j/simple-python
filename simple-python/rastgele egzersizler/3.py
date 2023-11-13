# verilen onluk sistemdeki bir sayıyı ikilik sistemdeki bir sayıya çeviren program


def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

decimal_number = 20
binary_number = decimal_to_binary(decimal_number)
print(f"{decimal_number} --- {binary_number}")
