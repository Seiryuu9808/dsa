# Hoán đổi để khôi phục tính chất max-heap cho cây con gốc tại i
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


def heap_sort(arr):
    n = len(arr)
    # Tạo max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Lặp: đưa max (arr[0]) về cuối, rồi heapify lại phần còn lại [0..i-1]
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


