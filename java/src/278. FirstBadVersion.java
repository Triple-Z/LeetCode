public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        // 二分法
        return recursive(1, n);
    }

    private int recursive(int left, int right) {
        if (left >= right) return right;

        int mid = (right - left) / 2 + left;

        if (isBadVersion(mid)) {
            return recursive(left, mid);
        } else {
            return recursive(mid+1, right);
        }
    }
}