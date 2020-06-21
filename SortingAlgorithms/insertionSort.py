"""
Description 
Insertion sort involves finding the right place for a given element in a sorted list. So in beginning we compare the first 
two elements and sort them by comparing them. Then we pick the third element and find its proper position among the previous 
two sorted elements. This way we gradually go on adding more elements to the already sorted list by putting them in their 
proper position.
"""

def insertion_sort(InputList):
    for i in range(1, len(InputList)):
        j = i-1
        nxt_element = InputList[i]
        
        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j+1] = InputList[j]
            j=j-1
        InputList[j+1] = nxt_element

list = [3,6,2,6,7,9,10,11,45,67,43]
insertion_sort(list)
print(list)