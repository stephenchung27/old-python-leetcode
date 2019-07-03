# Disjoint set/Union find

class DSU:
    def __init__(self, length):
        self.sets = [i for i in range(length)]
    
    def find(self, x):
        if x != self.sets[x]:
            x = self.find(self.sets[x])

        return x
    
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)

        self.sets[xr] = yr

    def getCount(self):
        unique = set()

        for i in range(len(self.sets)):
            if i != self.sets[i]:
                unique.add(self.find(i))

        return len(unique)

dsu = DSU(8)
print(dsu.sets)

dsu.union(1, 2)
print(dsu.sets)

dsu.union(3, 4)
print(dsu.sets)

# dsu.union(2, 4)
print(dsu.sets)

print(dsu.find(1))
print(dsu.getCount())

print(dsu.find(0))