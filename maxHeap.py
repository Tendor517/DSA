import random
import time
import matplotlib.pyplot as plt


def max_heapify(arr, n, i):
    """
    Maintain max-heap property for subtree rooted at index i
    n = size of heap
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child exists and is larger
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is larger
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Swap and continue heapifying if root is not largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)
    return

def max_heap_sort(arr):
    n = len(arr)

    # Build max heap (bottom-up, O(n))
    for i in range(n // 2 - 1, -1, -1):  #n//2 - 1 gives the index of the last non-leaf node and n//2 gives the count of nodes that have at least one child
        max_heapify(arr, n, i)

    '''# Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move current root to end
        max_heapify(arr, i, 0)               # Heapify reduced heap'''

    return arr

if __name__ == "__main__":
    
    sizes = [100, 1000, 10000, 100000,1000000];times=[]
    for size in sizes:
        arr = [random.randint(0, 10) for _ in range(size)]
        start = time.perf_counter()
        max_heap_sort(arr)
        end = time.perf_counter()
        exec_time=end-start
        print(f"Heap sort for size {size}: {exec_time:.6f} seconds")
        times.append(exec_time)

    plt.plot(sizes, times, marker='o', markerfacecolor='red', markeredgecolor='red', color='blue',linestyle="--")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Execution Time vs Input Size")
    plt.grid(True, which="both", linestyle="--", linewidth=0.7)
    plt.show()