class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = [0] * (n + 1)

        for x, y in trust:
            count[x] -= 1 # trust someone
            count[y] += 1 # trusted by someone
        
        for i in range(1,n+1):
            if count[i] == n-1:
                return i

        return -1
