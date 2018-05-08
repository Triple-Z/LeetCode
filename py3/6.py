class Solution:
	def convert(self, s, numRows):
		"""
		:type s: str
		:type numRows: int
		:rtype: str
		"""

		if numRows == 1:
			return s

		queue = list()
		for i in range(0, numRows):
			queue.append(list())

		h = 0
		forward = True
		for char in s:
			# print(queue)
			if forward:
				if 0<= h < numRows-1 :
					queue[h].append(char)
					h += 1
				elif h == numRows-1:
					queue[h].append(char)
					h -= 1
					forward = False
			else:
				if 0 < h <= numRows-1 :
					queue[h].append(char)
					h -= 1
				elif h == 0:
					queue[h].append(char)
					h += 1
					forward = True

		rstr = ""
		for sub_queue in queue:
			for char in sub_queue:
				rstr += char
		
		return rstr
			

solution = Solution()
# print("The string is: ")
print(solution.convert("PAYPALISHIRING", 3))
print(solution.convert("AB", 1))
		

