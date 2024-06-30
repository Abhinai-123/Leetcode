class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.count = n 

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            # Union by rank
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1
            self.count -= 1
            return True
        return False

    def connected_components(self):
        return self.count

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf_alice = UnionFind(n)
        uf_bob = UnionFind(n)
        
        edges = [[t, u - 1, v - 1] for t, u, v in edges]

        removable_edges = 0

        for edge in edges:
            if edge[0] == 3:
                if not uf_alice.union(edge[1], edge[2]):
                    removable_edges += 1  
                else:
                    uf_bob.union(edge[1], edge[2])  

        for edge in edges:
            if edge[0] == 1:
                if not uf_alice.union(edge[1], edge[2]):
                    removable_edges += 1  

        for edge in edges:
            if edge[0] == 2:
                if not uf_bob.union(edge[1], edge[2]):
                    removable_edges += 1  

        if uf_alice.connected_components() > 1 or uf_bob.connected_components() > 1:
            return -1  

        return removable_edges
