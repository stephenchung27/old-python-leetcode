'''
Change Making Problem

The Change Making Problem asks what is the fewest number of coins you can use to make a certain amount, if you have coins of a certain set of denominations. 
You can use any quantity of each denomination, but only those denominations. 
'''

import math
def coins(denominations, target):
    cache = {}
    def subproblem(i, t):
        if (i, t) in cache:
            return cache[(i, t)]  # memoization
        # Compute the lowest number of coins we need if choosing to take a coin
        # of the current denomination.
        val = denominations[i]
        if val > t:
            choice_take = math.inf  # current denomination is too large
        elif val == t:
            choice_take = 1  # target reached
        else:
            choice_take = 1 + subproblem(i, t - val)  # take and recurse
        # Compute the lowest number of coins we need if not taking any more
        # coins of the current denomination.
        choice_leave = (
            math.inf if i == 0  # not an option if no more denominations
            else subproblem(i - 1, t))  # recurse with remaining denominations
        optimal = min(choice_take, choice_leave)
        cache[(i, t)] = optimal
        print(cache)
        return optimal
    return subproblem(len(denominations) - 1, target)

coins([1, 2, 3], 5)