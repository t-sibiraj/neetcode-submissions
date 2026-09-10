class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        coloumn_title = []

        while columnNumber > 0:
            columnNumber -= 1
            remainder, quotient  = columnNumber % 26, columnNumber // 26
            coloumn_title += chr(ord('A') + remainder)
            columnNumber = quotient


        return ''.join(coloumn_title[::-1])





        