class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1

        def binary_search(low, high, target):
            mid = (low + high) // 2

            # print(low, mid, high)
            if mid == low or mid == high:
                if nums[high] < target:
                    return high + 1
                elif nums[low] > target:
                    return low
                elif nums[low] < target <= nums[high]:
                    return high
            
            if nums[mid] > target:
                high = mid
                return binary_search(low, high, target)
            elif nums[mid] < target:
                low = mid
                return binary_search(low, high, target)
            elif nums[mid] == target:
                # print(mid)
                return mid
            

        index = binary_search(low, high, target)

        return index