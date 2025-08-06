class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        breakpoint()
        if n == 1:
            return [i for i in range(10)]
        
        ans = []
        def backtrack(n, cur_num):
            breakpoint()
            if n == 0:
                return ans.append(cur_num)
            
            else:
                tail_digit = cur_num % 10
                next_digits = set([tail_digit + k, tail_digit - k])
                
                for next_digit in next_digits:
                    if 0 <= next_digit < 10:
                        new_num = cur_num * 10 + next_digit
                        backtrack(n-1, new_num)
                        
        for num in range(1, 10):
            backtrack(n-1, num)

        return list(ans)

if __name__ == "__main__":
    s = Solution()
    n = 3
    k = 7
    print(s.numsSameConsecDiff(n, k))