class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        final_string = ""
        word1_length = len(word1)
        word2_length = len(word2)

        pt1 = 0
        pt2 = 0

        add_from_first = True
        add_from_second = True

        while True:
            if add_from_first:
                final_string += word1[pt1]
            
            if add_from_second:
                final_string += word2[pt2]

            pt1 += 1
            pt2 += 1

            if pt1 >= word1_length:
                add_from_first = False
            
            if pt2 >= word2_length:
                add_from_second = False

            if not add_from_first and not add_from_second:
                break

        return final_string
        