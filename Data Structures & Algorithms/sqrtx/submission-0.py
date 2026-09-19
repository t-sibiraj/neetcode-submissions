class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x

        while start <= end:
            middle = (start + end) // 2

            if middle ** 2 < x:
                start = middle + 1

            elif middle ** 2 > x:
                end = middle - 1

            else:
                return middle

        return start - 1