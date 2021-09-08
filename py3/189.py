class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        
        ans = [0 for _ in range(n)]
        for i in range(n):
            ans[(i+k)%n]=nums[i]
        
        for i in range(n):
            nums[i] = ans[i]
        
        return