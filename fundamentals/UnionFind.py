class UnionFind:
    """
    QuickUnion with path compression and union by rank
    also added a `count` variable to help with algorithms
    where we are looking for the number of groups
    """
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            if self.rank[x] > self.rank[y]:
                self.root[y] = x
            elif self.rank[y] > self.rank[x]:
                self.root[x] = y
            else:
                self.root[y] = x
                self.rank[x] += 1
            self.count -= 1
            return True
        return False

    def connected(self, x, y):
        return self.find(x) == self.find(y)
