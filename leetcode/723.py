class Solution:
    def candyCrush(self, board):
        n, m = len(board), len(board[0])

        crushable = True
        while crushable:
            crushable = False
            for r in range(n):
                for c in range(m):
                    if board[r][c] == 0: 
                        continue

                    # Vertical
                    count = 1
                    for offset in range(1, n - r):
                        if abs(board[r + offset][c]) == abs(board[r][c]):
                            count += 1
                        else:
                            break

                    if count >= 3:
                        crushable = True
                        for offset in range(0, count):
                            board[r + offset][c] = -abs(board[r + offset][c])

                    # Horizontal
                    count = 1
                    for offset in range(1, m - c):
                        if abs(board[r][c + offset]) == abs(board[r][c]):
                            count += 1
                        else:
                            break

                    if count >= 3:
                        crushable = True
                        for offset in range(0, count):
                            board[r][c + offset] = -abs(board[r][c + offset])

            for r in reversed(range(n)):
                for c in range(m):
                    if board[r][c] < 0:
                        offset = 1
                        while r - offset >= 0 and board[r - offset][c] < 0:
                            offset += 1
                        if r - offset >= 0 and board[r - offset][c] > 0:
                            board[r][c], board[r - offset][c] = board[r - offset][c], board[r][c]

            for r in range(n):
                for c in range(m):
                    if board[r][c] < 0:
                        board[r][c] = 0

        return board


s = Solution()
board = [[110, 5, 112, 113, 114], [210, 211, 5, 213, 214], [310, 311, 3, 313, 314], [410, 411, 412, 5, 414], [5, 1, 512,
                                                                                                              3, 3], [610, 4, 1, 613, 614], [710, 1, 2, 713, 714], [810, 1, 2, 1, 1], [1, 1, 2, 2, 2], [4, 1, 4, 4, 1014]]

for r in board:
    print(r)

for r in s.candyCrush(board):
    print(r)
