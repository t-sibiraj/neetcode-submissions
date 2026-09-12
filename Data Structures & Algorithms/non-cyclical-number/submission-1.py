class Solution:
    def calculate_sum_of_squares_of_digit(self, number: int) -> int:
        total = 0

        while number > 0:
            digit = number % 10
            total += (digit ** 2)
            number = number // 10

        return total

    def isHappy(self, n: int) -> bool:


        seen_before = set()


        while n != 1:
            if n in seen_before:
                return False
            
            seen_before.add(n)
            n = self.calculate_sum_of_squares_of_digit(n)


        return True





