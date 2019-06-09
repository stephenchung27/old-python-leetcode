'''
You are given an array of million numbers and provided a range of index (say left, right). 
For multiple queries, each with input left and right indexes, output the maximum in that range.

Obvious choice would be to iterate from left to right and find the max
Additional optimization would be the memoize the maximum for that range
Whenever an input encompasses that range, use the memo for that specific portion
'''

