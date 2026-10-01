class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:

        length = len(pairs)
        answer = []

        for i in range(length):
            j = i -1

            while j >= 0 and pairs[j].key > pairs[i].key:
                j -= 1
            
            popped_element = pairs.pop(i)
            pairs.insert(j+1, popped_element)
            
    

            
            
            answer.append(pairs[:])

        return answer