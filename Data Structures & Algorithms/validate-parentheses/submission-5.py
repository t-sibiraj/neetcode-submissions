class Solution:
    def isValid(self, s: str) -> bool:


        if not s:
            return False

        st = []
        closing_opening_bracket = {
            ')' : "(",
            '}' : "{",
            ']' : "["
        }


        for parenthesis in s:
            if parenthesis in closing_opening_bracket:
                if st and st[-1] == closing_opening_bracket[parenthesis]:
                    st.pop()
                else:
                    return False
            else:
                st.append(parenthesis)

        if st:
            return False
        else:
            return True


        