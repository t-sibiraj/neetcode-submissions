class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        length  = len(nums)     
        sum = length

        for i in range(length):
            sum += (i - nums[i])
        
        return sum