import numpy as np

# Hàm ghép hai mảng đã được sort lại với nhau
def merge(a, b):
    # Độ dài của 2 mảng
    n = len(a)
    m = len(b)
    i = 0
    j = 0
    k = 0
    dtype = np.result_type(a, b)
    ans = np.empty(n + m, dtype=dtype)
    # Ghép hai mảng lại với nhau bằng 2 con trỏ
    while (i < n and j < m):
        if (a[i] < b[j]):
            ans[k] = a[i]
            i += 1
        else:
            ans[k] = b[j]
            j += 1
        k += 1

    # Thêm các phần tử còn thừa mà vòng lặp trên chưa xử lý
    if i < n:
        ans[k : k + (n - i)] = a[i:n]
    if j < m:
        ans[k : k + (m - j)] = b[j:m]
    return ans

# Hàm thực hiện phép chia để trị
def divide(a, l, r):
    # Khi mảng chỉ có 1 phần tử trả về nó
    if (l == r):
        return a[l : l + 1]
    # Chia đôi đoạn [l, r] qua phần tử mid
    mid = (l + r) >> 1
    f = divide(a, l, mid)
    g = divide(a, mid + 1, r)
    # Trả về 2 mảng f, g được merge
    return merge(f, g)


def merge_sort(arr):
    if arr is None or len(arr) == 0:
        return arr
    return divide(arr, 0, len(arr) - 1)



