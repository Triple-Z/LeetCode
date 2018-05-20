class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        snums = nums.copy()
        snums.sort()
        start, end = len(nums), 0
        for i in range(0, len(nums)):
            if snums[i] != nums[i]:
                start = min(start, i)
                end = max(end, i)

        if end - start < 0:
            return 0
        else:
            return end - start + 1
