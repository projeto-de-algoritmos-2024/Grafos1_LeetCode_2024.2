from collections import deque
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        fila = deque([(0, 0, health - grid[0][0])])
        visitado = {}
        print(grid)
        while fila:
            x, y, vida_atual = fila.popleft()
            
            if (x, y) == (m - 1, n - 1):
                if vida_atual  > 0:
                    return True
            
            for dx, dy in direcoes:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n:
                    vida_atualizada = vida_atual - grid[nx][ny]
                    
                    if vida_atualizada > 0 and vida_atualizada > visitado.get((nx, ny), 0):
                        visitado[(nx, ny)] = vida_atualizada
                        fila.append((nx, ny, vida_atualizada))
                        
                        print(f"Movimento| [{x}, {y}] -> [{nx}, {ny}] | Vida Atual {vida_atualizada}")
                        
        return False
