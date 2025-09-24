import random
import time
from itertools import accumulate
import matplotlib.pyplot as plt

def countSort(arr, stable=False):
    # Since values are always in [0, 10]
    value_spread = 11 #since we only gonna use random.randint(0,10) for now, so direct input for speedier execution
    min_val = 0

    # Step 1: Count occurrences (O(n))
    count = [0] * value_spread
    for num in arr:
        count[num] += 1

    # Step 2: Prefix sums → starting indices (O(k))
    start_index = list(accumulate(count))
    start_index = [0] + start_index[:-1]

    # Step 3: Build output (O(n))
    output = [0] * len(arr)
    if stable:
        for num in reversed(arr):   # stable
            output[start_index[num]] = num
            start_index[num] -= 1
    else:
        for num in arr:             # not stable (slightly faster)
            output[start_index[num]] = num
            start_index[num] += 1

    # Step 4: Update in place
    arr[:] = output


if __name__=='__main__':
    sizes = [100, 1000, 10000, 100000, 1000000]
    times = []

    for size in sizes:
        arr = [random.randint(0, 10) for _ in range(size)]
        start = time.perf_counter()
        countSort(arr, stable=False)  # use stable=True if needed
        end = time.perf_counter()
        exec_time = end - start
        print(f"Counting sort for size {size}: {exec_time:.6f} seconds")
        times.append(exec_time)

    plt.plot(sizes, times, marker='o', markerfacecolor='red',
             markeredgecolor='red', color='blue', linestyle="--")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Counting Sort Execution Time vs Input Size [Range 0–10]")
    plt.grid(visible=True, which="both", linestyle="--", linewidth=0.7)
    plt.show()




'''def countSort(arr, start_index):
    output = [0]*len(arr)
    for j in arr:
        output[start_index[j]] = j
        start_index[j] += 1
    arr[:] = output  # overwrite the contents of arr, not the variable itself


if __name__=='__main__':
    
    arr=[1,0,3,1,3,1]
    value_spread=(max(arr)-min(arr))+1
    start_index=[0]*value_spread
    start_index = [arr.count(i) for i in range(value_spread)]
    start_index=list(accumulate(start_index))
    start_index=[0]+start_index[:-1]
    print(f"value range and it's starting indices= {start_index}")
    countSort(arr,start_index)
    print(arr)'''