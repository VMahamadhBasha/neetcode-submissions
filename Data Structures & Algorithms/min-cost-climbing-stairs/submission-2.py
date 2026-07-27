class Solution:
    def minCostClimbingStairs(self, c: List[int]) -> int:
        n=len(c)
        dp=[0]*(n+1)
        for i in range(2,len(c)+1):
            dp[i]=min(dp[i-1]+c[i-1],dp[i-2]+c[i-2])
        return dp[n]