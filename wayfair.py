A = [2, 2, 3, 4, 3, 3, 2, 2, 1, 1, 2, 5]
B = [2, 2, 3, 4, 3, 3]
C = [2, 2, 3, 4]
D = [2, 2, 2]

def solution(A):
    if len(A) == 1: return 1
        
    start = 1

    while start < len(A) - 1 and A[0] == A[start]:
        start += 1

    if start == len(A) - 1: 
        return 1
    
    going_up = False if A[0] < A[start] else True

    count = 0

    for i in range(start, len(A)):
        if going_up and A[i - 1] > A[i]:
            count += 1
            going_up = False
        elif not going_up and A[i - 1] < A[i]:
            count += 1
            going_down = True
    
    return count

print(solution(A))
print(solution(B))
print(solution(C))
print(solution(D))g