class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        length  = len(nums)
        all_the_numbers = list(range(length+1))
        
        for num in all_the_numbers:
            if num not in nums:
                return num