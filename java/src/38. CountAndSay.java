class Solution {
    public String countAndSay(int n) {
        String ans = "";
        for (int i = 1; i <= n; i++) {
            ans = getNextString(i, ans);
        }
        return ans;
    }

    private String getNextString(int n, String pre) {
        if (n == 1) return "1";

        // get next string
        int i = 0;
        // regs
        int count = 0, num = 0, curNum = 0;
        StringBuilder sb = new StringBuilder();
        while (i < pre.length()) {
            curNum = pre.charAt(i) - '0';
            if (curNum == num) {
                count++;
            } else if (num != 0) {
                sb.append(Integer.toString(count));
                sb.append(Integer.toString(num));
                num = curNum;
                count = 1;
            } else {
                num = curNum;
                count = 1;
            }
            i++;
        }
        // clear buf
        sb.append(Integer.toString(count));
        sb.append(Integer.toString(num));

        return sb.toString();
    }
}