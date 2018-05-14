class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # max_num = nums[0]

        # for i in range(1, len(nums)):
        #     nums[i] = max(nums[i], nums[i-1] + nums[i])
        #     max_num = max(nums[i], max_num)
        
        # return max_num

        # Kadane's Algorithm
        max_so_far = max_ending_here = nums[0]
        for num in nums[1:]:
            max_ending_here = max(num, num + max_ending_here)
            max_so_far = max(max_ending_here, max_so_far)
        
        return max_so_far
