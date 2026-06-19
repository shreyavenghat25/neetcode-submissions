class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # go from last digit to first
        for i in range(len(digits) - 1, -1, -1):

            # if digit is less than 9, just add 1 and done
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # if digit is 9, set it to 0 and carry over
            digits[i] = 0

        # if we are here all digits were 9
        # add 1 at the front
        return [1] + digits