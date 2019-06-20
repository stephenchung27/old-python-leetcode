def n_queens(n):
    def backtrack(row):
        if row == n:
            results.append(col_placement.copy())
            return
        for col in range(n):
            if all(abs(c - col) not in (0, row - i) for i, c in enumerate(col_placement[:row])):
                col_placement[row] = col
                backtrack(row + 1)
    
    results = []
    col_placement = [0] * n
    backtrack(0)
    return results


print(n_queens(4))
