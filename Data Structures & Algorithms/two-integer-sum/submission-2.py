class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:



        

        # {
        #     3 : 0
        # }

        number_index = {}
        index = 0
        for num in nums:
            difference = target - num # 7 - 4 = 3

            if difference in number_index:
                # if 3 in number_index

                # return [0, 1]
                return [number_index[difference], index]
            else:
                number_index[num] = index
            # number_index[3] = 0

            index += 1

       



        