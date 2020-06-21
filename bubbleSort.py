"""
Description 
It is a comparison-based algorithm in which each pair of adjacent elements is compared and the elements are swapped if 
they are not in order.
"""

def bubblesort(list):
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp

list = [10,9,8,7,6,5,4,3,2,1]
bubblesort(list)
print(list)