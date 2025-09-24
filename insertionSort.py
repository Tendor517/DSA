import random
import time
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]   # shift right
            j -= 1
        arr[j + 1] = key          # place key
    return arr

if __name__ == "__main__":
    sizes=[100, 1000, 10000,100000,1000000];times=[]
    for size in sizes:  # don’t try 1000000 with insertion sort!
        arr = [random.randint(0, 10) for _ in range(size)]
        
        start = time.perf_counter()
        sorted_arr = insertion_sort(arr)
        end = time.perf_counter()
        exec_time=end - start
        print(f"Array size {size}: {exec_time:.6f} seconds")
        times.append(exec_time)
        
        
    plt.plot(sizes, times, marker='o', markerfacecolor='red', markeredgecolor='red', color='blue',linestyle="--")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Execution Time vs Input Size")
    plt.grid(True, which="both", linestyle="--", linewidth=0.7)
    plt.show()




