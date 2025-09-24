import random
import time
import matplotlib.pyplot as plt


def min_heapify(arr, n, i):
    """
    Maintain min-heap property for subtree rooted at index i
    n = size of heap
    """
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child exists and is smaller
    if left < n and arr[left] < arr[smallest]:
        smallest = left

    # Check if right child exists and is smaller
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    # Swap and continue heapifying if root is not smallest
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)

def min_heap_sort(arr):
    n = len(arr)

    # Build min heap (bottom-up)
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i)

    '''# Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move current root (smallest) to end
        min_heapify(arr, i, 0)           # Heapify reduced heap'''

    return arr

if __name__ == "__main__":
    sizes = [100, 1000, 10000, 100000,1000000];times=[]
    for size in sizes:
        arr = [random.randint(0, 10) for _ in range(size)]
        start = time.perf_counter()
        min_heap_sort(arr)
        end = time.perf_counter()
        exec_time=end-start
        # print("Sorted in descending order:", arr)
        print(f"Execution time: {exec_time:.6f} seconds")
        times.append(exec_time)
        
    plt.plot(sizes, times, marker='o', markerfacecolor='red', markeredgecolor='red', color='blue',linestyle="--")
    plt.xscale("log") #log base 10 is used
    plt.yscale("log")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Execution Time vs Input Size")
    plt.grid(True, which="both", linestyle="--", linewidth=0.7)
    plt.show()