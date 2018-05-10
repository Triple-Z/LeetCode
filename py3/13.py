class Solution:
	def romanToInt(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		sum = 0
		for i, char in enumerate(s):
			# print(i, char, sum)
			if char in ('V', 'X') and i-1 >= 0 and s[i-1] == 'I':
				sum += {
					'V': 3,
					'X': 8,
				}.get(char)
			elif char in ('L', 'C') and i-1 >= 0 and s[i-1] == 'X':
				sum += {
					'L': 30,
					'C': 80,
				}.get(char)
			elif char in ('D', 'M') and i-1 >= 0 and s[i-1] == 'C':
				sum += {
					'D': 300,
					'M': 800,
				}.get(char)
			else:
				sum += {
					'I': 1,
					'V': 5,
					'X': 10,
					'L': 50,
					'C': 100,
					'D': 500,
					'M': 1000,
				}.get(char)
			
		return sum

# solute = Solution()
# print(solute.romanToInt("MMMCDXC"))
