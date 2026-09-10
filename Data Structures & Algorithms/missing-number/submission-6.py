class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        length = len(nums)

        xorr = length

        for i in range(length):
            xorr ^= (i ^ nums[i])
        
        return xorr