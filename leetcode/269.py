from collections import defaultdict


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        def recurse(words):
            if len(words) == 1:
                return

            l = r = 0

            while r < len(words):
                if words[l][0] != words[r][0]:
                    adj_list[words[l][0]].append(words[r][0])

                    group = [word[1:] for word in words[l:r] if len(word) > 1]

                    if len(group) > 0:
                        recurse(group)

                    l = r
                r += 1
            if l != r:
                recurse([word[1:] for word in words[l:r] if len(word) > 1])

        def dfs(l, cur="", visited=None):
            if visited is None:
                visited = set()

            if l not in adj_list:
                if len(cur + l) == len(adj_list):
                    return cur + l
                else:
                    return ""

            if l in visited:
                return ""

            visited.add(l)

            return max([dfs(c, cur + l, set(visited)) for c in adj_list[l] if adj_list[l]], key=len, default='')

        adj_list = {}
        for letter in set("".join(words)):
            adj_list[letter] = []

        recurse(words)
        print(adj_list)
        return dfs(words[0][0])
