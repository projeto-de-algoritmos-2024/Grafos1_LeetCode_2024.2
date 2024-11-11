class Solution:
    def findChampion(self, n: int, arestas: List[List[int]]) -> int:
        grau_entrada = [0] * n
        adjacencias = [[] for _ in range(n)]
        
        for u, v in arestas:
            adjacencias[u].append(v)
            grau_entrada[v] += 1
        
        candidatos = [i for i in range(n) if grau_entrada[i] == 0]
        
        if len(candidatos) != 1:
            return -1
        
        campeao = candidatos[0]
        
        for i in range(n):
            if i != campeao and grau_entrada[i] == 0:
                return -1
        
        return campeao
