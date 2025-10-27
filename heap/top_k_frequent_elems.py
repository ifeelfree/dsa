import heapq
from collections import Counter

def heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

def build_min_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    return arr

def demo_heapq():
    heap = [5, 2, 8]
    heapq.heapify(heap)
    print(heapq.heappop(heap))

def demo_self_heapq():
    a_list = [5, 2, 8]
    new_list = build_min_heap(a_list)
    print(new_list[0])

def top_k_frequent_heap(arr, k):
    freq = Counter(arr)
    heap = [(-count, -num, num) for num, count in freq.items()]
    heapq.heapify(heap)
    result = []
    for _ in range(k):
        result.append(heapq.heappop(heap)[2])
    return result


if __name__ == "__main__":
    demo_heapq()
    demo_self_heapq()

    arr = [3, 1, 4, 4, 5, 2, 6, 1]
    k = 2
    print(top_k_frequent_heap(arr, k))  # Output: [4, 1]




