class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        buy=prices[0]
        for price in prices:
            buy=min(buy,price)
            maxp=max(maxp,price-buy)
        return maxp