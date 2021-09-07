class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        
        i = 0  # slow pointer
        for j in range(1, len(nums)):  # fast pointer
            if nums[i] != nums[j]:
                i = i + 1
                nums[i] = nums[j]
        
        return i + 1