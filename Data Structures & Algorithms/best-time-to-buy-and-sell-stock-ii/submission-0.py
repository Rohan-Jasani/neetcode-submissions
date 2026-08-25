class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        for i in range(0, n-1):
            if (pro:=prices[i+1] - prices[i]) > 0:
                profit+=pro
        return profit