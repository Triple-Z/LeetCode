class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        overflow = False

        if len(digits) == 1:
            overflow = True

        for i in range(len(digits)-1, -1, -1):
            if i == len(digits)-1 and i:
                # Plus one
                digits[i] += 1
                if digits[i] >= 10:
                    overflow = True
                    digits[i] %= 10
                else:
                    overflow = False
            elif i > 0:
                if overflow:
                    digits[i] += 1
                    if digits[i] >= 10:
                        overflow = True
                        digits[i] %= 10
                    else:
                        overflow = False
            elif i == 0:
                if overflow:
                    digits[i] += 1
                    if digits[i] >= 10:
                        # Extend
                        overflow = True
                        digits[i] %= 10
                        new_digits = [0 for _ in range(len(digits)+1)]
                        new_digits[0] = 1
                        new_digits[1:] = digits
                        digits = new_digits
                    else:
                        overflow = False

        return digits
