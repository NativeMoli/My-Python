


def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):  # проходимо список кілька разів
        for j in range(n - i - 1): # кожен раз проходимо до останнього невідсортованого елемента
            if arr[j] > arr[j + 1]: # якщо поточний елемент більший за наступний
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # міняємо їх місцями
    return arr