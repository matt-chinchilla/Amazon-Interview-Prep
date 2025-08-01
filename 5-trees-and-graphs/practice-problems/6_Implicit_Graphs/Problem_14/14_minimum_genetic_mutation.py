from typing import List
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        da_bet = ['A','C','G','T']
        
        def neighbors(gene):      
            one_away = []
            
            for i in range(len(gene)):
                nucleotide = gene[i]
                for mutation in da_bet:
                    if mutation == nucleotide:
                        pass
                    nucleotide = mutation
                    new_gene = gene[:i] + nucleotide + gene[i + 1:]
                    if new_gene in bank:
                        one_away.append(new_gene)
            return one_away

        queue = deque([(startGene, 0)])
        seen = set(startGene)
        
        while queue:
            gene, steps = queue.popleft()
            if gene == endGene:
                return steps
            
            for neighbor in neighbors(gene):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, steps + 1))
        return -1
            
if __name__ == "__main__":
    sol = Solution()
    startGene = "AACCGGTT"
    endGene = "AAACGGTA"
    bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
    print(sol.minMutation(startGene, endGene, bank))