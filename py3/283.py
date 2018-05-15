class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Bubble sort (Time Limit Exceeded)
        # for i in range(len(nums)-1, -1, -1):
        #     for j in range(0, i):
        #         if nums[j] == 0:
        #             nums[j], nums[j+1] = nums[j+1], nums[j]
        
        # Custom algorithm
        cur_len = origin_len = len(nums)

        if origin_len > 1:

            for num in nums:
                if num == 0:
                    cur_len -= 1

            i = 0
            while i <= cur_len and len(nums) > i:
                if nums[i] == 0:
                    nums.pop(i)
                    if len(nums) == 0:
                        break
                else:
                    i += 1
            
            for i in range(0, origin_len-cur_len):
                nums.append(0)


