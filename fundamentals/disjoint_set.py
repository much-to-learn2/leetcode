class QuickFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        """
        return the root node of a given node
        """
        return self.root[x]

    def union(self, x, y):
        """
        merge two nodes
        """
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class QuickUnion:    
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        """
        return the root node of a given node
        have to climb the parent tree until you find root
        """
        while x != root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        """
        merge two nodes
        if their root nodes aren't equal, set the
        root of Y equal to the root of X
        """
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            root[rootY] = rootX

    def connected(self, x, y):
        """
        check if two nodes are connected
        """
        return self.find(x) == self.find(y)


class QuickUnionByRank:
    """
    QuickUnion optimized to Union by rank.
    """
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        rootX = self.find(X)
        rootY = self.find(Y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.root[rootY] > self.rank[rootX]:
                self.root[rootX] = self.rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class QuickUnionPathCompressionOptimization:
    """
    Quick Union implementation with path compression
    """
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        if self.root[x] == x:
            return x
        
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self, x, y ):
        return self.find(x) == self.find(y)


class QuickUnionOptimized:
    """
    QuickUnion with path compression and union by rank
    """
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
