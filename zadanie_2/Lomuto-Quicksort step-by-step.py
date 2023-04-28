import numpy as np
import time
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

def quicksort_doublechecked(arr, lo, hi):
    # Ensure indices are in correct order
    if lo >= hi or lo < 0:
        return 0
    elif lo < hi:
        p = partition_doublecheck(arr, lo, hi)

        #  Sort partitions reqursively
        quicksort(arr, lo, p - 1)
        quicksort(arr, p + 1, hi)

def partition(arr, lo, hi):
    pivot = arr[hi] # Last element as the pivot
    i = lo
    for j in range(lo, hi):
        if arr[j] < pivot:
            # print("[Swap] "+str(arr[i])+" >< "+str(arr[j]))
            arr[i], arr[j] = arr[j], arr[i] # Swap
            i += 1
    arr[i], arr[hi] = arr[hi], arr[i] # swap
    return i

def partition_doublecheck(arr, lo, hi):
    pivot = arr[hi] # Last element as the pivot
    i = lo
    for j in range(lo, hi):
        if arr[j] < pivot and arr[i] != arr[j]:
            # print("[Swap] "+str(arr[i])+" >< "+str(arr[j]))
            arr[i], arr[j] = arr[j], arr[i] # Swap
            i += 1
    arr[i], arr[hi] = arr[hi], arr[i] # swap
    return i


if __name__ == "__main__":
    A = np.random.randint(-100,100,50)
    B = np.copy(A)
    low, high = 0, len(A)-1

    # Test for standard Lomuto
    start_a = time.time()
    # print("BEFORE SORTING:", A)
    quicksort(A, low, high)
    # print("\nAFTER SORTING:", A)
    end_a = time.time()
    diff_a = end_a - start_a
    # print("\nTime passed: " + str(diff_a))

    # Test for doublechecked
    start_b = time.time()
    # print("BEFORE SORTING:", B)
    quicksort_doublechecked(B, low, high)
    # print("\nAFTER SORTING:", A)
    end_b = time.time()
    diff_b = end_b - start_b
    # print("\nTime passed: " + str(diff_b))

    # # Summary
    # diff_total = str(abs(diff_a - diff_b))
    # if diff_a > diff_b:
    #     quicker="a"
    # else:
    #     quicker="b"
    
    # print("Total difference between two algos: " + diff_total)
    # if quicker=="a":
    #     print("Partitioning without condition to omit nonproductive swaps is quicker by")
    #     print(str(diff_a/diff_b*100)+"%")
    # else:
    #     print("Partitioning with condition to omit nonproductive swaps is quicker by ")
    #     print(str(diff_b/diff_a*100)+"%")

    # Generalization
    def standardLomuto(m):
        n = np.random.randint(1,m)
        A = np.random.randint(-100,100,n)
        low, high = 0, len(A)-1
        start_a = time.time()
        quicksort(A, low, high)
        end_a = time.time()
        diff_a = end_a - start_a
        return diff_a

    def doublecheckedLomuto(m):
        n = np.random.randint(1,m)
        A = np.random.randint(-100,100,n)
        low, high = 0, len(A)-1
        start_a = time.time()
        quicksort_doublechecked(A, low, high)
        end_a = time.time()
        diff_a = end_a - start_a
        return diff_a
         
    sum_standard, sum_doublechecked = 0, 0
    trials=10000 # No of array pairs to test
    m = 100 # No of numbers in an array
    for i in range(1, trials):
        sum_standard += standardLomuto(m)
        sum_doublechecked += doublecheckedLomuto(m)

    av_standard = sum_standard / trials
    print("Mean time for standard Lomuto: "+str(av_standard))
    av_doublcheck = sum_doublechecked / trials
    print("Mean time for Lomuto doublechecked: "+str(av_doublcheck))

    # Generalized summary
    # Summary
    av_diff = str(abs(av_standard - av_doublcheck))
    if av_standard > av_doublcheck:
        quicker="a"
        print("Standard was quicker by average.")
    else:
        quicker="b"
        print("Doublechecked was quicker by average.")
    
    print("\nMean difference between two algos: " + av_diff)
    if quicker=="a":
        print("In a series of "+str(trials)+" trials, for a pair of array of length="+str(m)+" partitioning without condition to omit nonproductive swaps averages ")
        print(str(av_standard/av_doublcheck*100)+"% speed of the alternative.")
    else:
        print("In a series of "+str(trials)+" trials, for a pair of array of length="+str(m)+" partitioning with condition to omit nonproductive swaps averages ")
        print(str(av_doublcheck/av_standard*100)+"% speed of the alternative.")
