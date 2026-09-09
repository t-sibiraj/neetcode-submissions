import math
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        st = []
        # add all the alnum characters
        for character in s:
            if character.isalnum():
                st.append(character.lower())

        start = 0
        end = len(st) - 1
        mid = (len(st) // 2) - 1
        print(mid)
        while start <= mid:
            # print(s[end], s[start])
            if st[end] != st[start]:
                return False

            start += 1
            end -= 1
        
        return True


# 0 1 2 3 4 5 6 
        
