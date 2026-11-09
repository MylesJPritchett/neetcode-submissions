class Solution:
    def rob(self, nums: List[int]) -> int:

        if(len(nums) < 3):
            return max(nums)


        return max(self.rob_line(nums[1:]), self.rob_line(nums[:-1]))


    def rob_line(self, houses):
        dp = [houses[0], max(houses[0], houses[1])]
        for i in range(2, len(houses)):
            dp.append(max(dp[i-1], dp[i-2] + houses[i]))
    
        return dp[-1]