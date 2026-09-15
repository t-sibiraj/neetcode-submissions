class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # {
        #     1: 1
        #     2 : 1
        # }

        # me = 1

        # [1,2,3,2,2,2,5,4,2]

        hashmap = {}
        majority_element = nums[0]
        for num in nums:
            if num in hashmap:
                hashmap[num] = hashmap[num] + 1
            else:
                hashmap[num] = 1

            if hashmap[num] > hashmap[majority_element]:
                    majority_element = num

        
        return majority_element
        