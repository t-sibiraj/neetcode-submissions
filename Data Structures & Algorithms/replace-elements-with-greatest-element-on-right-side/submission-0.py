class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        answer = [0] * len(arr)
        # answer[len(arr) - 1] = arr[len(arr) - 1]
        answer[len(arr) - 1] = -1

        for index in range ( len(arr)-1, -1, -1):
            max_element = max(arr[index] , answer[index])
            answer[index - 1] = max_element
        
        answer[-1] = -1

        return answer
            
        