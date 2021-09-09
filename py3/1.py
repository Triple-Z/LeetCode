class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = dict()
        
        for i in range(len(nums)):
            adder = target - nums[i]
            if num_map.get(adder) is not None:
                return [num_map[adder], i]
            else:
                num_map[nums[i]] = i
        
        return []
