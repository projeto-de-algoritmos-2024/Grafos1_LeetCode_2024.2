class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        fila = deque(initialBoxes)
        doces = 0
        chaves = set() # se no indice i = 
        caixas_visitadas = set(initialBoxes) 
        caixas_abertas = set() 

        while fila:
            caixa = fila.popleft()
            if caixa in caixas_abertas: 
                continue

            if status[caixa] == 1 or caixa in chaves: # se caixa pode ser aberta ou tem chave
                caixas_abertas.add(caixa)
                doces += candies[caixa]

                # indexar chaves achadas na caixa

                for chave in keys[caixa]:    # chave = indice da caixa
                    if chave not in chaves:
                        chaves.add(chave)

                # verificar se a key encontrada é de alguma caixa já visitada
                
                        if chave in caixas_visitadas and chave not in caixas_abertas:
                            fila.append(chave)
                
                # caixas dentro de caixa

            for containedBox in containedBoxes[caixa]:
                if containedBox not in caixas_visitadas:  # marca como visitado 
                    caixas_visitadas.add(containedBox)
                if (status[containedBox] == 1 or containedBox in chaves) :
                    fila.append(containedBox)

        return doces
