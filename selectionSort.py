
import random
import time
import matplotlib.pyplot as plt

def selectionSort(arr):
    for i in range(len(arr)):
        min_value_index = i
        # find the minimum in the rest of the array
        for j in range(i+1, len(arr)):
            if arr[min_value_index] > arr[j]:
                min_value_index = j   # only update index, don't swap yet
        
        # swap after inner loop ends
        arr[i], arr[min_value_index] = arr[min_value_index], arr[i]
    return arr

if __name__ == '__main__':
    sizes=[100,1000,10000,100000,1000000];times=[]
    for size in sizes:
       arr=[random.randint(0,10) for _ in range(size)]
       start = time.perf_counter()
       selectionSorted = selectionSort(arr)
       end = time.perf_counter()
       exec_time=end - start
       print(f"Execution time: {exec_time:.6f} seconds")
       times.append(exec_time)
    plt.plot(sizes, times, marker='o', markerfacecolor='red', markeredgecolor='red', color='blue',linestyle="--")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Execution Time vs Input Size")
    plt.grid(True, which="both", linestyle="--", linewidth=0.7)
    plt.show()