'''
Given an unsorted array, return the numbers that can be found with binary search.
Time complexity: O(n)
'''

# Current iteration is O(logn)
def binarySearchable(arr):
    def leftSearch(start, end, prev):
        if start > end: return
        mid = (start + end) // 2
        if arr[mid] <= arr[prev]: nums.append(arr[mid])
        else: return
        
        leftSearch(start, mid - 1, mid)
        rightSearch(mid + 1, end, mid)

    def rightSearch(start, end, prev):
        if start > end: return
        mid = (start + end) // 2
        if arr[mid] >= arr[prev]: nums.append(arr[mid])
        else: return
        
        leftSearch(start, mid - 1, mid)
        rightSearch(mid + 1, end, mid)
    
    mid = len(arr) // 2
    nums = [arr[mid]]
    leftSearch(0, mid - 1, mid)
    rightSearch(mid + 1, len(arr) - 1, mid)

    return nums

print(binarySearchable([1, 2, 1, 4, 4, 5, 1, 1, 1, 1]))

