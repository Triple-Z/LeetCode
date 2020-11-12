class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ans = new LinkedList<>();

        List<Integer> numList = IntStream.of(nums).boxed().collect(Collectors.toList());

        backtrack(ans, numList, nums.length, 0);
        return ans;
    }

    private void backtrack(List<List<Integer>> ans, List<Integer> numList, int n, int first) {
        if (first == n) {
            ans.add(new ArrayList<>(numList));
        }

        for (int i = first; i < n; i++) {
            Collections.swap(numList, first, i);
            backtrack(ans, numList, n, first + 1);
            // backtracking, swap back
            Collections.swap(numList, first, i);
        }
    }
}