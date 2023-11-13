# Bir array'deki elemanların toplamını bulan program
# Farklı bir yaklaşım ile

def sum(arr):
    sum = 0

    for i in arr:
        sum += i

    return sum


if __name__ == "__main__":
    arr = [35, 166, 93, 199, 200]
    toplam = sum(arr)

    print("{} listesinin toplamı: {}".format(arr, toplam))
