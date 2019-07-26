'''
Given a number n, find the smallest number that has same set of digits as n and is greater than n. 
If n is the greatest possible number with its set of digits, then print “not possible”.

https://leetcode.com/problems/next-permutation/
'''

def next_number(num):
    number = [int(digit) for digit in str(num)]
    N = len(number)

    start = N - 1

    while start > 0 and number[start - 1] >= number[start]:
        start -= 1

    if start == 0:
        return "Not possible."

    start -= 1
    
    value = number[start]
    next_index = start + 1

    while next_index < N - 1 and value < number[next_index + 1]:
        next_index += 1

    number[start], number[next_index] = number[next_index], number[start]

    l = start + 1
    r = N - 1
    while l < r:
        number[l], number[r] = number[r], number[l]
        l += 1
        r -= 1
    
    return int("".join(str(digit) for digit in number))


print(next_number(83091))
print(next_number(8203542))
print(next_number(34321))
print(next_number(4321))
print(next_number(1111))
print(next_number(0))
