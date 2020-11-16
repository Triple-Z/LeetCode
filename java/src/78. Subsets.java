class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new LinkedList<>();
        
        backtrack(ans, new ArrayList<>(), nums, 0);

        return ans;
    }

    private void backtrack(
        List<List<Integer>> ans,
        List<Integer> curList,
        int[] nums,
        int cur
    ) {
        // terminator
        if (cur == nums.length) {
            ans.add(new ArrayList<>(curList));
            return;
        }

        // choose this element
        curList.add(nums[cur]);
        backtrack(ans, curList, nums, cur+1);

        // backtracking
        // remove this element
        curList.remove(curList.size() - 1);
        backtrack(ans, curList, nums, cur+1);
    }
}