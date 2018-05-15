class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        for num in nums:
            if d.get(num):
                d[num] += 1
            else:
                d[num] = 1
        
        max_num, max_count = 0, 0
        for num, count in d.items():
            if count > max_count:
                max_num = num
                max_count = count
            if max_count >= len(nums)/2:
                return max_num
        
        return max_num
