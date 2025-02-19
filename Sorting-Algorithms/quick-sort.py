def quickSort(arr, l, r):
    if l < r:
        p = partition(arr, l, r)
        quickSort(arr, l, p - 1)
        quickSort(arr, p + 1, r)

def partition(arr, l, r):
    pivot = arr[r]  
    x = l  
    y = r - 1  

    while x <= y:
        
        while x <= y and arr[x] <= pivot:
            x += 1
        
        while x <= y and arr[y] > pivot:
            y -= 1
        
        if x <= y:
            arr[x], arr[y] = arr[y], arr[x]
            x += 1
            y -= 1

    
    arr[x], arr[r] = arr[r], arr[x]
    return x  

arr = [12, 11, 13, 5, 6, 7]
quickSort(arr, 0, len(arr)-1)
print(arr)  