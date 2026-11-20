class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Sliding Window Problem
        # Goal: You get 1 buy and 1 sell; while we're insider trading knowing future prices
        # we cannot break physics by buying or selling out of sequence.

        # I've learned that Sliding Window is a 2Ptr problem
        # let's just treat it like one.

        # The best approach is to set L at 0, R at L+1; check profit each day then
        # adjust points based on lowest buy and highest sell to max profit

        max_profit = 0 # if we choose not to buy, 0
        buy, sell = 0, 1
        best_buy = 0
        
        while sell < len(prices):
            # profitable?
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                if profit > max_profit:
                    max_profit = profit
            else:
                # Update buy if it's a better price
                buy = sell

            # always increment r after the check
            sell += 1

        return max_profit


        l, r = 0, 1
        best_buy, best_sell = None, None

        # probably not ideal
        while l in range(len(prices) - 2): # i cannot be == j
            while r in range(l, len(prices) - 1): # start, stop, step
                lPrice = prices[l]
                rPrice = prices[r]

                # worth buy
                if (lPrice - rPrice) > max_profit:
                    best_buy = l
                    best_sell = r
                # elif lPrice - rPrice < 0 and

                r += 1
            l += 1

        if best_buy is None: return 0

        return prices[best_sell] - prices[best_buy]

            

            