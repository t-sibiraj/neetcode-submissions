# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        start,end = 0,n

        while start <= end:
            middle = (start + end) // 2

            g = guess(middle)

            if g > 0:
                start = middle + 1
            elif g < 0:
                end = middle - 1
            else:
                return middle
        