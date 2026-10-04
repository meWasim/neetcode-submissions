class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum = 0

        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                res=prices[i+1] - prices[i]
                sum +=res
        
        return sum

        
# [7,1,5,3,6,4]

# 7-1= 6(loss)
# 1-5=4(profit)
# 3-6=3(profit)
# 6-4= loss()
# max profit is 7

