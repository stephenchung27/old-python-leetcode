'''
Given two integer arrays, find the longest common subsequence.

Example:
A = [1, 5, 2, 6, 3, 7]
B = [5, 6, 7, 1, 2, 3]
output = [1, 2, 3] or [5, 6, 7]
'''

def longest_common_subsequence(A, B):
    A_map = {n: i for i, n in enumerate(A)}
    B_map = {n: i for i, n in enumerate(B)}

    dp_A = [0] * len(A)
    dp_B = [0] * len(B)

    for i, num in enumerate(A):
        if i <= B_map[num]:
            dp_A[i] = 1
    
    for i, num in enumerate(B):
        if i <= A_map[num]:
            dp_B[i] = 1

    return max([A[i] for i, a in enumerate(dp_A) if a == 1], [B[i] for i, a in enumerate(dp_B) if a == 1], key=len)


A = [1, 5, 2, 6, 3, 7, 4, 8]
B = [5, 6, 7, 1, 2, 3, 4, 8]

print(longest_common_subsequence(A, B))
