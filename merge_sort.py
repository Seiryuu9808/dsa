# Hàm ghép hai mảng đã được sort lại với nhau
def merge(a, b):
    ans = []
    # Độ dài của 2 mảng
    n = len(a)
    m = len(b)
    i = 0
    j = 0
    # Ghép hai mảng lại với nhau bằng 2 con trỏ
    while (i < n and j < m):
        if (a[i] < b[j]):
            ans.append(a[i])
            i+=1
        else:
            ans.append(b[j])
            j+=1
            
    # Thêm các phần tử còn thừa mà vòng lặp trên chưa xử lý
    while (i < n):
        ans.append(a[i])
        i += 1
    while (j < m):
        ans.append(b[j])
        j += 1
    return ans

# Hàm thực hiện phép chia để trị
def divide(a, l, r):
    # Khi mảng chỉ có 1 phần tử trả về nó
    if (l == r):
        return [a[l]]
    # Chia đôi đoạn [l, r] qua phần tử mid
    mid = (l + r) >> 1
    f = divide(a, l, mid)
    g = divide(a, mid + 1, r)
    # Trả về 2 mảng f, g được merge
    return merge(f, g)


def merge_sort(arr):
    if not arr:
        return []
    return divide(arr, 0, len(arr) - 1)



