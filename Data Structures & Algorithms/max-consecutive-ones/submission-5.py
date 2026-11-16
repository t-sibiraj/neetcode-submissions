class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive_one_so_far = 0
        consecutive_one_counter = 0

        for num in nums:
            if num == 1:
                consecutive_one_counter += 1
            else:
                if consecutive_one_counter >= max_consecutive_one_so_far:
                    max_consecutive_one_so_far = consecutive_one_counter
                consecutive_one_counter = 0 # reset back to zero

        if consecutive_one_counter >= max_consecutive_one_so_far:
            max_consecutive_one_so_far = consecutive_one_counter
        
        return max_consecutive_one_so_far
        
        