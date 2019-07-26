'''
Given a binary tree where the nodes values are letters, return the word that is first if sorted all words lexicographically.
So, imagine a root with val of 'a' that has two children. 

One nodes value is 'b' and the other 'c'. 
They both have no children. 
The words you would get back is `ca` & `ba`. 

So, because lexicographically `ba` is smaller/first, the return value of the method would be `ba`.
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

def solution(root):
    word = None

    def dfs(root, curr):
        if not root:
            word = min(word, curr)
            return
        
        for child in root.children:
            dfs(child, root.val + curr)

    dfs(root)
    return word