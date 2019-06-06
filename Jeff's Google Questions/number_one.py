'''
You are given a 2D array with 0s and 1s.
Return the length of the longest line of 1s.
Lines can be horizontal, diagonal, or vertical.

If the dimensions are n x m, you get O(nm) time complexity.
You would need to do a pass for every direction:
    1. Rows
    2. Columns
    3. Left-to-right diagonal
    4. Right-to-left diagonal

The optimizations lie in the fact that once you have a max you can skip iterations
where sum of the current number of 1s and the number of remaining elements is shorter 
than that length.

Similarly, you can skip the diagonals closer to the corners that are shorter than the max.
'''