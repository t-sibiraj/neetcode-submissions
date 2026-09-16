class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_day_price_index = 0
        sell_day_price_index = 1


        while sell_day_price_index < len(prices):
            if prices[buy_day_price_index] < prices[sell_day_price_index]:
                profit = max(profit, prices[sell_day_price_index] - prices[buy_day_price_index] )
            else:
                buy_day_price_index = sell_day_price_index
            

            sell_day_price_index += 1

        return profit
        