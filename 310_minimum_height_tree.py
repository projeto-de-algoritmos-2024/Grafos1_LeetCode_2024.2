# MHTs = minimum height trees (MHTs

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        # verificar se é nó sozinho(raiz)
        if n == 1 or not edges:
            return [0]

        graph = {i: [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        MHTs = [node for node in graph if len(graph[node]) == 1]

        while n > 2:
            n -= len(MHTs)
            proxFolhas = []

            for leaf in MHTs:
                u = graph[leaf][0]  
                graph[u].remove(leaf)  
                if len(graph[u]) == 1:
                    proxFolhas.append(u)

            MHTs = proxFolhas

        return MHTs
