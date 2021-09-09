class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        
        i, j = 0, 0
        # i to find zeros
        # j to find non-zeros
        while i < n and j < n:
            if nums[i] != 0 and nums[j] != 0:
                i += 1
                j += 1
            elif nums[i] != 0 and nums[j] == 0:
                i += 1
            elif nums[i] == 0 and nums[j] != 0:
                # swap nums[i] and nums[j]
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i += 1
                j += 1
            else:
                j += 1