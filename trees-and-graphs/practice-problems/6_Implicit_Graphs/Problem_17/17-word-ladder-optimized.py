from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        visited = set()
        twords = set(wordList)
        
        bw,ew = beginWord, endWord
        if endWord not in twords:
            return 0

        begin_set,end_set, next_set = set(),set(), set()
        begin_set.add(bw)
        end_set.add(ew)
        dist = 0

        while begin_set and end_set: 
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
            next_set = set()
            dist +=1
            for word in begin_set:
                word_chars = list(word)
                for i in range(len(word_chars)):
                    ochar = word_chars[i]
                    for j in range(26):
                        word_chars[i] = chr(ord('a')+j)
                        changed_word = "".join(word_chars)
                        if changed_word in end_set:
                            return dist+1                    
                        if (changed_word not in visited) and (changed_word in twords):
                            next_set.add(changed_word)
                            visited.add(changed_word)

                        word_chars[i] = ochar
            begin_set = next_set
                
        return 0
        

if __name__ == "__main__":
    sol = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(sol.ladderLength(beginWord, endWord, wordList))
