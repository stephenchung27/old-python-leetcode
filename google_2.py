[1, 2, 3, 4, 5]

[1, 2, 3, 4]
[2, 3, 4, 5]

A = [1, 1, 1, 1, 2] k = 3
B = [6, 4, 3, 6, 5, 2, 6, 3, 3] k = 3
C = [1, 1, 1, 1]
D = [1, 4, 3, 2, 5]
E = [1, 1, 1]


def find_larger(A, B):
    for i in range(len(A)):
        if A[i] != B[i]:
            if A[i] > B[i]:
                return A
            else:
                return B

def find_largest_k_length_contiguous_subarray(A, k):
    if k > len(A): return []
    if k == len(A): return A

    max_array = [0] * k

    for i in range(len(A) - k + 1):
        for j in range(k):
            if max_array[j] < A[i + j]:
                max_array = A[i:i + k]
                break
            if max_array[j] > A[i + j]:
                break
    
    return max_array


def find_largest_k_length_contiguous_subarray(A, k):
    if k > len(A): return None
    if k == len(A): return A

    max_index = 0

    for i in range(0, len(A) - k + 1):
        for j in range(k):
            if A[max_index + j] < A[i + j]:
                max_index = i
                break
            elif A[max_index + j] > A[i + j]:
                break
    
    return A[max_index:max_index+k]


print(find_largest_k_length_contiguous_subarray(A, 3))
print(find_largest_k_length_contiguous_subarray(B, 3))
print(find_largest_k_length_contiguous_subarray(C, 3))
print(find_largest_k_length_contiguous_subarray(D, 4))
print(find_largest_k_length_contiguous_subarray(E, 2))
