import random

# Hàm chia mảng theo pivot (<= pivot bên trái, > pivot bên phải)
def partition(arr, low, high):
    # Chọn pivot ngẫu nhiên
    pivot_idx = random.randint(low, high)
    # Swap pivot ra vị trí cuối cùng trong danh sách
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
    pivot = arr[high]
    
    # Dồn các phần tử <= pivot về bên trái
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Đưa pivot về đúng vị trí
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def helper(arr, low, high):
    # Điều kiện dừng đệ quy
    if low < high:
        # Lưu vị trí chính xác của pivot hiện tại
        pi = partition(arr, low, high)
        # Đệ quy sắp xếp hai nửa
        helper(arr, low, pi - 1)
        helper(arr, pi + 1, high)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    helper(arr, 0, len(arr) - 1)
    return arr


