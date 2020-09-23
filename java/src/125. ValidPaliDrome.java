class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        // remove other characters
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            if ((c >= 'a' && c <= 'z') || (c >= '0' && c <= '9')) {
                sb.append(c);
            }
        }
        String newStr = sb.toString();
        // two pointers
        int i = 0, j = newStr.length()-1;
        while (i < j) {
            if (newStr.charAt(i) != newStr.charAt(j)) {
                return false;
            }
            i++; j--;
        }

        return true;
    }
}