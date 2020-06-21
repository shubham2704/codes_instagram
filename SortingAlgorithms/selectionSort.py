"""
Description 
In selection sort we start by finding the minimum value in a given list and move it to a sorted list. 
Then we repeat the process for each of the remaining elements in the unsorted list. The next element entering the sorted 
list is compared with the existing elements and placed at its correct position. So at the end all the elements from the 
unsorted list are sorted.
"""

def selection_sort(l):

    for idx in range(len(l)):

        min_idx = idx
        for j in range( idx +1, len(l)):
            if l[min_idx] > l[j]:
                min_idx = j
        l[idx], l[min_idx] = l[min_idx], l[idx]


l = [19,2,31,45,30,11,121,27]
selection_sort(l)
print(l)