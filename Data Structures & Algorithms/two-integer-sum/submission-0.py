class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}

        for index in range(len(nums)):
            difference = target - nums[index]

            if difference in d:
                return [d[difference], index]
            
            d[nums[index]] = index
            


        