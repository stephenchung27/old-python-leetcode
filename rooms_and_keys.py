'''
Note that no function signature is given, and no args. You have to come up with it yourself during the interview, and solve the question end to end in about 40 mins.

You have a 2D maze that's composed of rooms. Each room has doors to the rooms next to it. Eg, a room in the middle of the maze will have 4 doors to the adjacent rooms. Some doors are unlocked which would allow you to go freely between the rooms. On the other hand, some doors are locked with a key; you can go through that door only if you have the corresponding key. Some rooms have keys laying around (for other rooms), which you can collect upon entering that room and use later on to unlock those doors.

The question is, given a starting and ending rooms, you need to return true only if it's possible to navigate the maze from start to end.
'''

def solve(maze):
    n, m = len(maze), len(maze[0])

    