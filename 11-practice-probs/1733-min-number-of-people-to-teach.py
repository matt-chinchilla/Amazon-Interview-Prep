from typing import List, Any
from collections import defaultdict, deque

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages = [set()] + [set(ls) for ls in languages]#type:ignore
        friend_circle = defaultdict(list)
        
        for u, v in friendships:
            if languages[u].isdisjoint(languages[v]):#type:ignore
                friend_circle[u].append(v)
                friend_circle[v].append(u)
                
        bad_users = set(friend_circle.keys())
        if not bad_users:
            return 0
        
        lang_count = [0] * (n + 1)
        for person in bad_users:
            for lang in languages[person]:
                lang_count[lang] += 1
                
        return len(bad_users) - max(lang_count)
      
if __name__ == "__main__":
    s = Solution()
    number_different_languages = 3
    languages = [[2],[1,3],[1,2],[3]]
    friendships = [[1,4],[1,2],[3,4],[2,3]]
    print(s.minimumTeachings(number_different_languages, languages, friendships))