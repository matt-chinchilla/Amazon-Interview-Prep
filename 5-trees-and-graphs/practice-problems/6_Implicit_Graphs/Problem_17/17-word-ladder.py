from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def neighbors(word):
            one_away = []
            # breakpoint()
            for i in range(len(word)):
                letter = word[i]
                for j in range(len(wordList)):
                    compareWord = wordList[j]
                    if letter == compareWord[i]:
                        pass
                    else:
                        new_word = word[:i] + compareWord[i] + word[i+1:]
                        if new_word in wordList:
                            one_away.append(new_word)
            return one_away
        
        # breakpoint()
        queue = deque([(beginWord, 1)])
        seen = set([beginWord])
        
        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            
            for neighbor in neighbors(word):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, steps+1))
                    
        return 0
    
if __name__ == "__main__":
    sol = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(sol.ladderLength(beginWord, endWord, wordList))