'''
A street is represented as an array.
The street has many blocks.
Each block has a list of stores on it.

You are given a list of required stores and a street.
Return the block you would want to live on to minimize the distance from the further requirement.

Personal thoughts:
This is an ambiguous question... Where can your house lie?

1. If the house can be placed anywhere where there isn't a store, you can use two pointers from
   the left and right. Keep a track of all stores that you visit with their indices. 
2. If you encounter the same store, update the pointers to account for the duplicate.
3. Once your two pointers touch, check if you encountered an empty space
    a. If you did, calculate the distance from that space to the furthest store
       This would only require checking the store's index with the pointers
       If there are multiple stores pick the one that's closest to the center
    b. If you didn't, the house can live on either side
       Find the empty spot closest to either of the two pointers
       The distance from that spot to the pointer on the opposite side is the distance
4. Find the min of the blocks using the distance calculated

1. If you house can only be placed at the beginning of the block, you can iterate through the 
   entire array until you visited every required store.
2. 
'''

def best_place_on_block(arr):
