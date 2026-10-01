class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:

        length = len(pairs)
        answer = []
        

        # the issue with this approach when we use range(1, length) is that
        # we always assume the list has atleast one element thats why we start with 1

        # empty list special condition
        if not pairs:
            return pairs

        answer.append(pairs[:])

        for i in range(1,length):
            j = i

            while j > 0 and pairs[j-1].key > pairs[j].key:
                pairs[j], pairs[j-1] = pairs[j-1], pairs[j]
            
                j -= 1
            
            answer.append(pairs[:])

        return answer