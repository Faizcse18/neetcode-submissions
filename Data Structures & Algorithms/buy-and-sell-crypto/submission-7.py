class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        faiz_profit=0

        while r < len(prices):
            if prices[l]<prices[r]:
                profit = prices[r]-prices[l]

                faiz_profit=max(faiz_profit,profit)
            else:
                l=r
             
            r+=1

        return faiz_profit
