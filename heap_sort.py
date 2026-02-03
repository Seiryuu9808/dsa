import heapq

def heap_sort(arr):
    # Biến danh sách thành heap
    heapq.heapify(arr)
    ans = []
    # Lấy các phần tử nhỏ nhất hiện tại của heap
    for i in range (len(arr)):
        ans.append(heapq.heappop(arr))
    return ans


