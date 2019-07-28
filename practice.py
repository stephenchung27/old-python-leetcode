import random

def quick_select(array, k):

    def select(l, r):
        if r == l:
            return array[l]
        
        pivot_index = random.randint(l, r)

        array[l], array[pivot_index] = array[pivot_index], array[l]

        i = l
        for j in range(l + 1, r + 1):
            if array[j] < array[l]:
                i += 1
                array[i], array[j] = array[j], array[i]
        
        array[i], array[j] = array[j], array[i]

        if k == i:
            return array[i]
        elif k < i:
            return select(l, i - 1)
        else:
            return select(i + 1, r)

    return select(0, len(array) - 1)


array = list(range(10, -1, -1))

quick_select(array, 5)

print(array)
