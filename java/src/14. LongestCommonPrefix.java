class Solution {
    public String longestCommonPrefix(String[] strs) {
        // corner case
        if (strs.length == 0) return "";
        if (strs.length == 1) return strs[0];

        int minLen = Integer.MAX_VALUE;
        for (String str : strs) {
            minLen = Math.min(minLen, str.length());
        }

        boolean flag = true;
        int prefixIndex = 0;
        for (int i = 0; i < minLen; i++) {
            char curCh = strs[0].charAt(i);            
            for (String str : strs) {
                if (str.charAt(i) != curCh) {
                    flag = false;
                    break;
                }
            }
            if (!flag) {
                prefixIndex = i;
                break;
            }
        }

        // if all match...
        if (flag) {
            prefixIndex = minLen;
        }

        if (prefixIndex <= 0) {
            return "";
        }
        return strs[0].substring(0, prefixIndex);
    }
}