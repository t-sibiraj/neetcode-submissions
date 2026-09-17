class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        pt1 = 0
        pt2 = 1

        while pt2  < len(nums):
            if nums[pt1] == nums[pt2]:
                nums.pop(pt2)

            else:
                pt1 += 1
                pt2 += 1

                


        
        return len(nums)



        