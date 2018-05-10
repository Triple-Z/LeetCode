class Solution:
	def isPalindrome(self, x):
		"""
		:type x: int
		:rtype: bool
		"""
		x_str = str(x)
		j = len(x_str) - 1
		for i in range(len(x_str) // 2 + 1):
			if i >= j:
				return True
			if x_str[i] == x_str[j]:
				j -= 1
			else:
				return False

solute = Solution()
print(solute.isPalindrome(11))
