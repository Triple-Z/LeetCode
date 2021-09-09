class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        nums.sort()
        for i in range(1, n, 2):
            if nums[i] != nums[i-1]:
                return nums[i-1]

        # n is odd, return the last element
        return nums[n-1]
