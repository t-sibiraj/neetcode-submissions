class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)

        suffix_max = [-1] * length

        for i in range(length-2,-1,-1):
            suffix_max[i] = max(suffix_max[i+1], arr[i+1])
        
        return suffix_max
            
        