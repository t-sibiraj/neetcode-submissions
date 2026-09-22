class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive_length = 0
        consecutive_length = 0

        for num in nums:
            if num == 1:
                consecutive_length += 1
                max_consecutive_length = max(consecutive_length, max_consecutive_length)
            else:
                consecutive_length = 0
        

        return max_consecutive_length






        