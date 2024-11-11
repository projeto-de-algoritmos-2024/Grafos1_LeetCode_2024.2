class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        
        grafo = collections.defaultdict(set)
        
        for i, j in edges:
            grafo[i].add(j)
            grafo[j].add(i)
        
        visitado = set()
        
        pilha = [(1, 0, 1.0)]  
        
        while pilha:
            no_atual, tempo_atual, probabilidade = pilha.pop()
            
            
            if tempo_atual >= t:
                if no_atual == target:
                    return probabilidade
                continue  
            
            visitado.add(no_atual)
            filhos = set(grafo[no_atual]) - visitado 
                
            if not filhos:
                if no_atual == target:
                    return probabilidade
                continue 
            
            probabilidade_filhos = probabilidade / len(filhos)
            
        
            for filho in filhos:
                pilha.append((filho, tempo_atual + 1, probabilidade_filhos))
        
        return 0 