class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return False
        
        num_map = dict()
        for i in nums:
            if num_map.get(i) is not None:
                return True
            else:
                num_map[i] = True

        return False