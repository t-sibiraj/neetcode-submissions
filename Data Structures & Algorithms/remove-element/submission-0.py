class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        no_of_elements = len(nums)
        no_of_val = 0

        index  = 0
        elements_encountered_so_far = 0

        while elements_encountered_so_far < no_of_elements:
            if nums[index] == val:
                added_to_the_back = nums.pop(index)
                nums.append(added_to_the_back)
                no_of_val += 1

            else:
                index += 1



            elements_encountered_so_far += 1

        return no_of_elements - no_of_val
        