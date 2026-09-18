class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        buy=prices[0]
        for i in prices:
            buy=min(buy,i)
            maxp=max(maxp,i-buy)
        return maxp