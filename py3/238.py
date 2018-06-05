class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        front = [ 1 for _ in range(length)]
        end = [ 1 for _ in range(length)]

        for i in range(length):
            if i == 0:
                front[0] = nums[0]
                end[length - 1] = nums[length - 1]
            else:
                front[i] = front[i-1] * nums[i]
                end[length - i - 1] = end[length - i] * nums[length - i - 1]

        rst = list()
        
        for i in range(length):
            if i == 0:
                rst.append(end[i+1])
            elif i == length - 1:
                rst.append(front[i-1])
            else:
                rst.append(front[i-1] * end[i+1])

        return rst
