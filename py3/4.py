class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if n > m:
            nums1, nums2, m, n = nums2, nums1, n, m

        if n == 0:
            if m % 2 == 1:
                return nums1[m//2]
            else:
                return (nums1[m//2 - 1] + nums1[m//2]) / 2
        
        imin, imax = 0, m
        while imin <= imax:
            i = (imin + imax) // 2
            j = (m + n + 1) // 2 - i
            # print(i, j)
            if (i == 0 or j == n or nums1[i-1] <= nums2[j]) and (i == m or j == 0 or nums1[i] >= nums2[j-1]):
                # i is the exact i
                if i == 0:
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    max_of_right = nums2[j]
                elif j == n:
                    max_of_right = nums1[i]
                else:
                    max_of_right = min(nums1[i], nums2[j])
                
                return (max_of_left + max_of_right) / 2.0

            elif (j > 0 and i < m) and nums2[j-1] > nums1[i]:
                imin += 1
            elif (i > 0 and j < n) and nums1[i-1] > nums2[j]:
                imax -= 1

# solute = Solution()
# print(solute.findMedianSortedArrays([1,2], [3,4]))
