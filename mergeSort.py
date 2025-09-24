import random
import time
import matplotlib.pyplot as plt

def mergeSort(arr,l,r):
    if l<r: #that is untill r>l
        mid=(l+r)//2
        mergeSort(arr,l,mid)
        mergeSort(arr,mid+1,r)
        merge(arr,l,mid,r)



def merge(arr,left,mid,right):
    n1 = mid - left + 1 #index range/size of left array
    n2 = right - mid    #index range/size of right array
    larr=[0]*n1
    rarr=[0]*n2

    #copy elements from the divided arrays
    for i in range(n1):
        larr[i]=arr[left+i]
    for j in range(n2):
        rarr[j]=arr[mid+1+j]
    
    i=0;j=0;k=left
    #to merge larr and rarr
    while i<n1 and j<n2: 
        if larr[i]<=rarr[j]: 
            arr[k]=larr[i]
            i+=1
        else:
            arr[k]=rarr[j]
            j+=1
        k+=1
    #reason for using the following two while blocks, for example consider merging [5,8,9] and [1,6,7]
    while i<n1:
        arr[k]=larr[i]
        i+=1;k+=1
    while j<n2:
        arr[k]=rarr[j]
        j+=1;k+=1


if __name__=="__main__":
    sizes = [100, 1000, 10000,100000,1000000];times=[]
    for size in sizes:
        arr=[random.randint(0,10) for _ in range (size)]
        start = time.perf_counter()
        mergeSort(arr,0,len(arr)-1)
        end = time.perf_counter()
        exec_time=end-start
        print(f"Merge sort for size {size}: {exec_time:.6f} seconds")
        times.append(exec_time)

    plt.plot(sizes, times, marker='o', markerfacecolor='red', markeredgecolor='red', color='blue',linestyle="--")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Execution Time vs Input Size")
    plt.grid(True, which="both", linestyle="--", linewidth=0.7)
    plt.show()