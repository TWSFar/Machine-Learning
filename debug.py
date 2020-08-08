import math

class Solution:
    def primePalindrome(self, N: int) -> int:
        dwss = [2, 3, 5, 7, 11]
        for v in dwss:
            if v >= N:
                return v
        while True:
            if len(str(N)) % 2 == 0:
                N = N * 6
            mod = N % 6
            isPrime = True
            ishw = True
            if mod == 1 or mod == 5:
                for i in range(2, math.ceil(math.sqrt(N))+1):
                    if N % i == 0:
                        isPrime = False
                        break
                temp = str(N)
                if temp[::-1] != temp:
                    ishw = False
                
                if isPrime and ishw:
                    return N
                N = N + 4 if mod == 1 else N + 2
            else:
                N = N + 1 if mod == 0 else N + 5 - mod


slt = Solution()

slt.primePalindrome(13)
