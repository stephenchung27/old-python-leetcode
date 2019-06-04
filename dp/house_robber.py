'''
House Robber Problem

In the House Robber Problem, you are a robber who has found a block of houses to rob. 
Each house i has a non-negative v(i) worth of value inside that you can steal. 
However, due to the way the security systems of the houses are connected, you’ll get caught if you rob two adjacent houses. 
What’s the maximum value you can steal from the block?
'''

# Time complexity: O(n)
# Space complexity: O(1) additional space
from typing import List
def house_robber(houses: List[int]) -> int:
    if len(houses) == 0: return None
    if len(houses) <= 2: return max(houses[0], houses[1])
    houses[2] = houses[0] + houses[2]
    for i in range(2, len(houses)):
        houses[i] = max(houses[i-2], houses[i-3]) + houses[i]
    return max(houses[-1], houses[-2])