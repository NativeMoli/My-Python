

def mean(arr):
    if not arr:
        return None
    return sum(arr) / len(arr)

def median(arr):
    if not arr:
        return None
    arr = sorted(arr)
    n = len(arr)
    mid = n // 2

    if n % 2 != 0:
        return arr[mid]
    else:
        return (arr[mid - 1] + arr[mid]) / 2