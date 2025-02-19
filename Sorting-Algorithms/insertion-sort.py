def InsertionSort(arr,n):
  for i in range(n):
    hold=arr[i]
    j=i-1
    while j>=0 and hold<arr[j]:
      arr[j+1]=arr[j]
      j-=1
    arr[j+1]=hold
  return arr
  
arr = [640, 34, 25, 12, 22, 11, 90]
n = len(arr)
print(InsertionSort(arr,n))



