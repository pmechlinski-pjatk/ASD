import numpy as np
# Za Cormen, Thomas H.; Leiserson, Charles E.; Rivest, Ronald L.; Stein, Clifford (2009) 
# Sorts a (portion of an) array, divides it into partitions, then sorts those

def quicksort(arr, lo, hi):
    # Ensure indices are in correct order
    if lo >= hi or lo < 0:
        return 0
    elif lo < hi:
        p = partition(arr, lo, hi)

        #  Sort partitions reqursively
        quicksort(arr, lo, p - 1)
        quicksort(arr, p + 1, hi)

def partition(arr, lo, hi):
    pivot = arr[hi] # Last element as the pivot
    i = lo
    for j in range(lo, hi):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i] # Swap
            i += 1
    arr[i], arr[hi] = arr[hi], arr[i] # swap
    return i


if __name__ == "__main__":
    A = np.random.randint(-100,100,50)
    low, high = 0, len(A)-1
    print("BEFORE SORTING:", A)
    quicksort(A, low, high)
    print("\nAFTER SORTING:", A)
