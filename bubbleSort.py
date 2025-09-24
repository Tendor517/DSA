import time
import random
import matplotlib.pyplot as plt

'''We sort the array using multiple passes. After the first pass,the maximum element goes to end 
(its correct position). Same way, after second pass, the second largest element goes to second last position and so on.'''

def bubbleSort(arr,n):
    for i in range(len(arr)):
            for j in range(0, n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                j+=1
    return
if __name__=='__main__':
    sizes=[100,1000,10000,100000,1000000]
    times=[]
    for size in sizes:
        arr=[random.randint(0,10) for _ in range (size)]
        start=time.perf_counter()
        bubbleSort(arr,len(arr))
        end=time.perf_counter();exec_time=end-start
        times.append(exec_time)
        print(f"Bubble sort for size {size}: {exec_time:.6f} seconds")