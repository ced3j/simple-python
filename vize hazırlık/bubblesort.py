def bubble_sort(arr):
    n = len(arr)

    # Tüm elemanları gez
    for i in range(n):
        # Her iterasyonda en büyük elamnı dizinin sonuna taşı

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


my_array = [64, 25, 12, 22, 11]
sorted_array = bubble_sort(my_array)
print(f"Sıralanmış dizi {my_array}")
