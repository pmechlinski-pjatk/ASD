
#%%
import random
import time
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# INSERTION - SORT

## Init data
ordered_list = list(range(1,1001))
unordered_list = list(reversed(ordered_list))
random_list = list()

i = 0
while i < 999:
    random_list.append(random.randint(1,1000))
    i += 1

## MAIN LOGIC
def insertion_sort(arr):
    a = arr
    n = len(a)
    i = 1
    for i in range(0, n):
        j = i
        while j > 0 and a[j-1] > a[j]:
            tmp = a[j]
            a[j] = a[j-1]
            a[j-1] = tmp
            j = j - 1
    return a

## TIME TESTS

### I. Ordered
start_ordered = time.time()
ord = insertion_sort(ordered_list)
end_ordered = time.time()
ordered_result = end_ordered - start_ordered
print("Ordered T: "+str(end_ordered - start_ordered))

### II. Unordered
start_unordered = time.time()
unord = insertion_sort(unordered_list)
end_unordered = time.time()
unordered_result = end_unordered - start_unordered
print("Unordered T: "+str(end_unordered - start_unordered))

### III. Random
start_random = time.time()
rando = insertion_sort(random_list)
end_random = time.time()
random_result = end_random - start_random
print("Random T: "+str(end_random - start_random))

## Visualisation
results = list()
results.append(ordered_result)
results.append(unordered_result)
results.append(random_result)

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
categories = ['Ordered', 'Unordered', 'Random']

ax.bar(categories, results)
