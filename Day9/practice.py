def s(arr, start, end):
    if(start<end):
        p = part(arr, start, end)
        s(arr, start, p-1)
        s(arr, p+1, end)

def part(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i+1

def quick_sort(arr):
    if not arr:
        return
    s(arr, 0, len(arr)-1)


if __name__ == "__main__":
    sample = [3,6,8,10,1,2,1]
    quick_sort(sample)
    print(sample)
    
    
    
    
    
def heap_sort(arr):
    n = len(arr)

    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


arr = [5, 3, 8, 4, 2, 7, 1, 6]

heap_sort(arr)

print(arr)    