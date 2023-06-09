import time
import numpy as np
# Python program for implementation of Quicksort Sort
 
# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot
 
 
# Function to find the partition position
def partition(array, low, high):
 
    # choose the rightmost element as pivot
    pivot = array[high]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort
 
 
def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)
 
 
# data = [1, 7, 4, 1, 10, 9, -2]
# # print("Unsorted Array")
# # print(data)
 
# size = len(data)
 
# quickSort(data, 0, size - 1)
 
# print('Sorted Array in Ascending Order:')
# print(data)

# Counting sort in Python programming


def countingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * 10000

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]


# data = [4, 2, 2, 8, 3, 3, 1]
# countingSort(data)
# # print("Sorted Array in Ascending Order: ")
# # print(data)

# Heap Sort in python


def heapify(arr, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
  
    if l < n and arr[i] < arr[l]:
        largest = l
 
    if r < n and arr[largest] < arr[r]:
        largest = r
  
    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
  
  
def heapSort(arr):
    n = len(arr)
  
    # Build max heap
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
  
    for i in range(n-1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]
  
        # Heapify root element
        heapify(arr, i, 0)
  
  
# arr = [1, 12, 9, 5, 6, 10]
# heapSort(arr)
# n = len(arr)
# # print("Sorted array is")
# # for i in range(n):
#     # print("%d " % arr[i], end='')
  
  
A = np.random.randint(1,1000,10000)
B = np.copy(A)
C = np.copy(A)

# print(A, B, C)

start_a = time.time()
quickSort(A, 0, len(A)-1)
end_a = time.time()
diff_a = (end_a - start_a) *1000

start_b = time.time()
countingSort(B)
end_b = time.time()
diff_b = (end_b - start_b) *1000

start_c = time.time()
heapSort(C)
end_c = time.time()
diff_c = (end_c - start_c) *1000

print("QuickSort: "+str(diff_a) + " ms")
print("CountingSort: "+str(diff_b) + " ms")
print("HeapSort: "+str(diff_c) + " ms")

