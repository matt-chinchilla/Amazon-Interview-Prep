from typing import List
from collections import defaultdict

class Solution:
	def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
		breakpoint()
		graph = defaultdict(list)

		for i in range(0, 10):
			if i - k >= 0:
				graph[i].append(i - k)
			if i + k < 10:
				graph[i].append(i + k)

		start = [i for i in graph if i != 0]

		for j in range(n - 1):
			new = set()

			for i in start:
				last = i % 10

				for k in graph[last]:
					new.add(i * 10 + k)

			start = new
		return list(start)

if __name__ == "__main__":
    s = Solution()
    n = 3
    k = 7
    print(s.numsSameConsecDiff(n, k))