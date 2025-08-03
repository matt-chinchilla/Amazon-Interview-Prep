class Solution:
    def maximum69Number (self, num: int) -> int:
        if num == 6:
            return 9
        n = len(list(str(num)))
        breakpoint()
        for i in range(1, n):
            num_str = str(num)
            for i, digit in enumerate(num_str):
                if digit == '6':
                    num_str = num_str[:i] + '9' + num_str[i+1:]
                    break
            num = int(num_str)
            break
        return num
if __name__ == "__main__":
    s = Solution()
    num = 9669
    n = len(list(str(num)))
    print(s.maximum69Number(num))