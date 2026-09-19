class Solution:
    def hammingWeight(self, n: int) -> int:
        no_of_1 = 0

        while n > 0:
            bit = n % 2
            if bit == 1:
                no_of_1 += 1
            
            n //= 2
        
        return no_of_1

        