class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = ""
        continue_search = True
        index = 0

        while index < len(strs[0]) and continue_search:
            character = strs[0][index]

            for individual_string in strs:
                if (index >= len(individual_string)
                        or individual_string[index] != character):
                    continue_search = False
                    break

            if continue_search:
                prefix += character

            index += 1

        return prefix