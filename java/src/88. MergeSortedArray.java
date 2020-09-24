class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if (n == 0) return;

        int i = 0, j = 0, k = 0;
        int[] nums1_copy = new int[m];
        System.arraycopy(nums1, 0, nums1_copy, 0, m);
        while (i < m && j < n) {
            if (nums1_copy[i] < nums2[j]) {
                nums1[k] = nums1_copy[i];
                i++;
            } else {
                nums1[k] = nums2[j];
                j++;
            }
            k++;
        }
        while (i < m) {
            nums1[k] = nums1_copy[i];
            i++; k++;
        }
        while (j < n) {
            nums1[k] = nums2[j];
            j++; k++;
        }
    }
}