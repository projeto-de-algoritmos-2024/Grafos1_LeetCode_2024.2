## vermelho = 1
## azul = 2

class Solution:

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def bfs(pessoa):
            queue = deque([pessoa])
            cor[pessoa] = 1
            
            while queue:
                atual = queue.popleft() # O(1)
                atual_cor = cor[atual]
                proxima_cor = 2 if atual_cor ==1 else 1

                for vizinho in grafo_dislike[atual]:
                    if vizinho not in cor:  # checa se ja foi pintado
                        cor[vizinho] = proxima_cor
                        queue.append(vizinho)
                    if cor[vizinho] == atual_cor:  # Se tem msm cor = n bi partido
                        return False
            return True

        grafo_dislike = [[] for _ in range(n+1)]
        cor = {}

        for i,j in dislikes:
            grafo_dislike[i].append(j)
            grafo_dislike[j].append(i)
        
        for pessoa in range(1, n+1):
            if pessoa in cor:
                continue
            if not bfs(pessoa):
                return False

        return True
            

            
