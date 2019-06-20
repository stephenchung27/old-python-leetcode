towers = [[4, 3, 2, 1], [], []]
moves = []

def towers_of_hanoi(n, start, end, aux):
    if n == 1:
        swap_towers(start, end)
        moves.append((start, end))
        return
    
    towers_of_hanoi(n-1, start, aux, end)
    swap_towers(start, end)
    moves.append((start, end))
    towers_of_hanoi(n-1, aux, end, start)
    
def swap_towers(start, end):
    towers[end].append(towers[start].pop())

print(towers)
towers_of_hanoi(len(towers[0]), 0, 2, 1)
print(towers)
print(moves)