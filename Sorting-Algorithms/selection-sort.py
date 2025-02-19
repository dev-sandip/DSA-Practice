def selectionSort(arr, n):
    for i in range(n):
        least = arr[i]
        pos = i
        for j in range(i+1, n):
            if arr[j] < least:
                least = arr[j]
                pos = j
        if pos != i:
            arr[i], arr[pos] = arr[pos], arr[i]
    return arr

arr = [64, 25, 12, 22, 11]
n = len(arr)
print(selectionSort(arr, n))