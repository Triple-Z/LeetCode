class Solution:
	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""

		if x >= 0:
			x_str = str(x)
			if x_str[-1] == '0' and len(x_str) > 1:
				x_str = x_str[:-1]
			rtn = x_str[::-1]
			y = int(rtn)
			if y > 2**31 - 1:
				return 0
			else:
				return y
		else:
			x_str = str(abs(x))
			if x_str[-1] == '0' and len(x_str) > 1:
				x_str = x_str[:-1]
			rtn =  '-' + x_str[::-1]
			y = int(rtn)
			if y < -2**31:
				return 0
			else:
				return y

# solute = Solution()
# print(solute.reverse(0))
