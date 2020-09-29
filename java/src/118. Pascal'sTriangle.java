class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ans = new ArrayList<>();
        if (numRows < 1) return ans;
        ans.add(Arrays.asList(1));
        if (numRows == 1) return ans;
        ans.add(Arrays.asList(1, 1));
        if (numRows == 2) return ans;

        for (int i = 2; i < numRows; i++) {
            // get last row
            List<Integer> lastRow = ans.get(i-1);
            // create current row
            List<Integer> curRow = new ArrayList<>(i+1);
            curRow.add(1);
            for (int j = 1; j < i; j++) {
                curRow.add(lastRow.get(j-1) + lastRow.get(j));
            }
            curRow.add(1);
            ans.add(curRow);
        }

        return ans;
    }
}