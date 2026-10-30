class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        result = 0
        for i in range(1, len(prices)):
            if prices[i] < min:
                min = prices[i]
            elif prices[i] - min > result:
                result = prices[i] - min
        print(result)
        return result