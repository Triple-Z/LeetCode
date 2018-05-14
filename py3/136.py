class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        hash_table = dict()

        for num in nums:
            try:
                hash_table.pop(num)
            except:
                hash_table[num] = 1
        
        return hash_table.popitem()[0]
