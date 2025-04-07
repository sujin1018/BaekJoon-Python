class Solution:
    def climbStairs(self, n: int) -> int:
        step = [0] * (n + 1)
        step[1] = 1
        if n >= 2:
            step[2] = 2
        for i in range(3, n+1):
            step[i] = step[i-2] + step[i-1]
        return step[n]