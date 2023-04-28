import numpy as np

def quicksort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
        quicksort(arr, lo, p - 1)
        quicksort(arr, p + 1, hi)

def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo
    for j in range(lo, hi):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[hi] = arr[hi], arr[i]
    return i


if __name__ == "__main__":
    A = np.random.randint(-100,100,50)
    low, high = 0, len(A)-1
    print("BEFORE SORTING:", A)
    quicksort(A, low, high)
    print("\nAFTER SORTING:", A)
