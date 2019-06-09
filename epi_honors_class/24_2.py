'''
Find the Missing Positive Entry

Design an algorithm to find the smallest positive integer which is not present in A.

Example: 
Input:  [3, 5, 4, -1, 5, 1, -1]
Output: 2
'''

def find_first_missing_positive(A):
    for i in range(len(A)):
        while 1 <= A[i] <= len(A) and A[i] != A[A[i] - 1]:
            A[A[i] - 1], A[i] = A[i], A[A[i] - 1]

    return next((i + 1 for i, a in enumerate(A) if a != i +1), len(A) + 1)

print(find_first_missing_positive([3, 5, 4, -1, 5, 1, -1]))
print(find_first_missing_positive([1, 2, 4, 5]))
print(find_first_missing_positive([1, 2, 3, 4, 5]))
print(find_first_missing_positive([1, 2, 3, 4, -1]))
