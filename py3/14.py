class Solution:
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		if len(strs) == 0:
			return ""

		min_len, prefix = len(strs[0]), ""
		for str in strs:
			if len(str) < min_len:
				min_len = len(str)
		
		for i in range(min_len):
			for j in range(len(strs)):
				if j == len(strs)-1 and strs[j][i] == strs[j-1][i]:
					prefix += strs[j][i]
				elif j == 0 or strs[j][i] == strs[j-1][i]:
					continue
				else:
					return prefix

		return prefix
