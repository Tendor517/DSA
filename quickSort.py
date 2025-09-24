import time
import random
import matplotlib.pyplot as plt
'''here we will have options= using last element/median of three/random element as pivot
using Lomuto Partition method'''

def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]
    return

#pivot index choice methods
def median_of_three(arr, low, high):
    mid = (low + high) // 2
    a, b, c = arr[low], arr[mid], arr[high]
    if a > b:
        if a < c:
            return low
        elif b > c:
            return mid
        else:
            return high
    else: #when a is not > b
        if a > c:
            return low
        elif b < c:
            return mid
        else:
            return high
def random_pivot(arr,low,high):
    idx = random.randint(0,high)  # inclusive both ends
    return idx
def last_element(arr,low,high):
    return high
pivot_choices={
    0:last_element,
    1:median_of_three,
    2:random_pivot
}

#performing quick sort algo and returning the pivot index
def partition(arr, low, high):
    # Example usage
    pivot= arr[high] #pivot element
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, high) #putting pivot element in correct positon between right and left
    return i + 1

def quickSort(arr,low,high):
    if low<high:  #that is untill there is only one element in array
        pi=partition(arr,low,high) #pivot index
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)


if __name__ == "__main__":
    sizes=[100,1000,10000,100000,1000000]
    times=[];flag=True
    for size in sizes:
        arr = [random.randint(1, 1000000) for _ in range(size)]
        if flag==True:
            choice = int(input("Pivot element choiceP:-\n0->last element\n1->median element\n2->random element = "))
            pivot_choice=pivot_choices.get(choice, lambda: print("Invalid choice"))(arr,0,len(arr)-1) #this second () calls the function object chosen from the dictionary
            swap(arr,pivot_choice,len(arr) - 1)  # Move chosen index to the end as pivot
            flag=False
        start=time.perf_counter()
        quickSort(arr, 0, len(arr) - 1)
        end=time.perf_counter()
        exec_time=end-start
        print(f"Quick sort for size {size}: {exec_time:.6f} seconds")
        times.append(exec_time)
    plt.plot(sizes,times,marker='o',markerfacecolor='red',markeredgecolor='red',linestyle='--')
    plt.xlabel("array size")
    plt.ylabel("execution time")
    plt.xscale("log")
    plt.yscale("log")
    plt.grid(visible=True,which='both',linestyle=':',lw='0.7')
    plt.show()
    print(f'Average time={sum(times)/5}')

