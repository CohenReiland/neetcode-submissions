class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        recent_min = None
        best = 0
        for n in prices:
            if  recent_min is None or n < recent_min:
                recent_min = n
            best = max(best, (n - recent_min))
        return best