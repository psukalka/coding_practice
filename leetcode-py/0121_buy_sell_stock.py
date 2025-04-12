"""
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

class Solution:
    def maxProfit(self, prices):
        """
        Profit will be maximum when we find two numbers whose difference is maximum
        Left number should be minimum and right number should be maximum 
        """
        return self.approach_2(prices)

    def approach_1(self, prices):
        """
        At any ith location find the minimum on its left
        """
        if len(prices) < 2:
            return 0
        
        if len(prices) == 2:
            return max(0, prices[1] - prices[0])
        
        max_profit = 0
        for idx, price in enumerate(prices):
            if idx < 1:
                continue
            if idx == 1:
                max_profit = max(max_profit, price - prices[0])
            left_min = min(prices[:idx])
            curr_profit = price - left_min
            if curr_profit > max_profit:
                max_profit = curr_profit
        return max_profit
    
    def approach_2(self, prices):
        """
        At any ith location find the minimum on its left
        
        We can do one optimisation. Since, we are shifting by just one number to right, 
        we don't need to find minimum of the whole left subset again. We can just compare it with current number. 
        If current number is less than minimum then that is the new min
        """
        if len(prices) < 2:
            return 0
        
        if len(prices) == 2:
            return max(0, prices[1] - prices[0])
        
        max_profit = 0
        left_min = None
        for idx, price in enumerate(prices):
            if idx < 1:
                continue
            if idx == 1:
                max_profit = max(max_profit, price - prices[0])
                left_min = prices[0]
            left_min = min(left_min, prices[idx-1])
            curr_profit = price - left_min
            if curr_profit > max_profit:
                max_profit = curr_profit
        return max_profit        

    def test_solution(self):
        assert 5 == self.maxProfit([7,1,5,3,6,4])
        assert 0 == self.maxProfit([[7,6,4,3,1]])
        print(f"Tests passed")
    
s = Solution()
s.test_solution()