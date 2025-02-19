def maxHeapify(arr,i,n):
  l = 2*i
  r = 2*i+1
  largest = i
  if l<n and arr[l]>arr[largest]:
    largest = l
  if r<n and arr[r]>arr[largest]:
    largest = r
  if largest!=i:
    arr[i],arr[largest] = arr[largest],arr[i]
    maxHeapify(arr,largest,n)

def buildMaxHeap(arr,n):
  for i in range(n//2,-1):
    maxHeapify(arr,i,n)


def heapSort(arr,n):
  buildMaxHeap(arr,n)
  for i in range(n-1,0,-1):
    arr[0],arr[i] = arr[i],arr[0]
    maxHeapify(arr,0,i)


arr = [12, 11, 13, 5, 6, 7]
heapSort(arr,len(arr))
print(arr)