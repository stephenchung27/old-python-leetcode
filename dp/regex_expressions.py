def isMatch(self, string: str, regex: str) -> bool:
    T = [[False] * (len(string) + 1) for _ in range(len(regex) + 1)]

    T[0][0] = True

    for i in range(1, len(T[0])):
        if regex[i - 1] == "*":
            T[0][i] = T[0][i - 2]

    for i in range(1, len(T)):
        for j in range(1, len(T[0])):
            if regex[j - 1] == "." or regex[j - 1] == string[i - 1]:
                T[i][j] = T[i - 1][j - 1]
            elif regex[j - 1] == "*":
                T[i][j] = T[i][j - 2]
                if regex[j - 2] == "." or pattern[j - 2] == string[i - 1]:
                    T[i][j] = T[i][j] or T[i - 1][j]
            else:
                T[i][j] = False

    return T[len(string)][len(regex)]
