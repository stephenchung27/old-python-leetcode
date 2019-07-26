'''
Given a graph of 3 x 3 where each node has an up/down/left/right and each node has a value from 1 - 9, count the number of possibilities.
'''

def count_pos(start, hops):
    count = 0

    def dfs(node, hops):
        if not node:
            return
        if hops == 0:
            count += 1

        for direction in node.directions:
            dfs(direction, hops - 1)

    dfs(start, hops)
    return count


def count_unique_pos(start, hops):
    count = 0
    visited = set()

    def dfs(node, hops, path):
        if not node:
            return

        # if path in visited:
        #     return

        # visited.add(path)

        if hops == 0:
            if path not in visited:
                visited.add(path)
                count += 1

        for direction in node.directions:
            dfs(direction, hops - 1, path + str(direction.val))

    dfs(start, hops, "")
    return count
