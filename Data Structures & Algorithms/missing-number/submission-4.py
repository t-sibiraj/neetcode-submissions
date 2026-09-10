class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        length  = len(nums)

        
        num_set = set(nums)

        for num in range(length+1):
            if num not in num_set:
                return num