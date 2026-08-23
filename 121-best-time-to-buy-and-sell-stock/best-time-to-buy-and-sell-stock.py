class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        buy=prices[0]
        for price in prices:
            if price<buy:
                buy=price
            else:
                maxp=max(maxp,price-buy)
        return maxp