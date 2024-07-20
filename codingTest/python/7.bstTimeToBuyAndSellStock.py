class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        # 초기화
        min = float('inf')
        max = 0

        for price in prices:
            if price < min:
                min = price

            elif price - min > max:
                max = price - min

        return max


print(Solution().maxProfit([3, 5, 9, 12]))  # 9
