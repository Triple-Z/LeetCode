class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ci = 1
        n = len(digits)
        for i in range(n):
            pos = n - i - 1
            new_val = digits[pos] + ci
            digits[pos] = new_val % 10
            ci = new_val // 10

        if ci > 0:
            digits.insert(0, 1)
        
        return digits