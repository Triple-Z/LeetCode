class Solution:
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		i = j = 0
		ans = 0
		sub_str = list()
		while i < len(s) and j < len(s):
			# Sliding window
			# Current window is [i, j)
			if s[j] not in sub_str:
				sub_str.append(s[j])
				ans = max(ans, j+1-i)
				j += 1
			else:
				sub_str.remove(s[i])
				i += 1

		return ans

solu = Solution()
print(solu.lengthOfLongestSubstring("abcabcbb"))
