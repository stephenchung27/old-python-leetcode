'''
function partition(list, left, right, pivotIndex)
    pivotValue := list[pivotIndex]
    swap list[pivotIndex] and list[right]  // Move pivot to end
    storeIndex := left
    for i from left to right-1
        if list[i] < pivotValue
            swap list[storeIndex] and list[i]
            increment storeIndex
    swap list[right] and list[storeIndex]  // Move pivot to its final place
    return storeIndex
'''

# def partition(array, left, right, pivotIndex):
#     pivotValue = array[pivotIndex]
#     array[pivotIndex], array[right] = array[right], array[pivotIndex]

#     storeIndex = left

#     for i in range(left, right - 1):
#         if array[i] < pivotValue:
#             array[storeIndex], array[i] = array[i], array[storeIndex]
#             storeIndex += 1
#     array[storeIndex], array[right] = array[right], array[storeIndex]

#     return storeIndex

# import random

# def quickSelect(array, left, right, k):
#     if len(array) == 1:
#         return array
    
#     pivotIndex = random.randint(left, right)

#     pivotIndex = partition(array, left, right, pivotIndex)

#     if k == pivotIndex:
#         return array[:k + 1]
#     elif k < pivotIndex:
#         return quickSelect(array, left, pivotIndex - 1, k)
#     else:
#         return quickSelect(array, pivotIndex + 1, right, k)

import random

def quickselect(array, k):

    def select(array, l, r, index):

        if r == l:
            return array[l]

        pivot_index = random.randint(l, r)

        array[l], array[pivot_index] = array[pivot_index], array[l]

        i = l
        for j in range(l+1, r+1):
            if array[j] < array[l]:
                i += 1
                array[i], array[j] = array[j], array[i]

        array[i], array[l] = array[l], array[i]

        if index == i:
            return array[i]
        elif index < i:
            return select(array, l, i-1, index)
        else:
            return select(array, i+1, r, index)

    return select(array, 0, len(array) - 1, k)

array = list(range(10, -1, -1))

quickselect(array, 5)

print(array[:5])
