class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> ans = new LinkedList<>();
        backtrack(ans, n, "", 0, 0);
        return ans;
    }

    private void backtrack(List<String> ans, int n, String pareString, int leftNum, int rightNum) {
        if (pareString.length() == n*2) {
            ans.add(pareString);
        } else {
            if (leftNum > n || rightNum > n) return;
            if (leftNum < n) {
                backtrack(ans, n, pareString + "(", leftNum+1, rightNum);
            }
            if (leftNum > rightNum) {
                backtrack(ans, n, pareString + ")", leftNum, rightNum+1);
            }
        }
    }
}