class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if target == nums[i] + nums[j] and i != j:
                    return [i, j]
