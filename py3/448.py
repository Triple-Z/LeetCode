class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            if nums[abs(nums[i])-1] > 0:
                nums[abs(nums[i])-1] *= -1
        
        ans = list()

        for i in range(0, len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        
        return ans
