class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:



        number_index = {}

        # {
        #     3 : 0
        # }
        index = 0
        for num in nums:
            difference = target - num # 7 - 3 = 4

            if difference in number_index:
                return [number_index[difference], index]
            
            number_index[num] = index
            # number_index[3] = 0

            index += 1

       



        