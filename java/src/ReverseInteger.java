class Solution {
    public int reverse(int x) {
        String intString = String.valueOf(x);
        
        StringBuilder sb = new StringBuilder();
        String rtnString = null;
        if (x < 0) {
            sb.append(intString.substring(1));
            sb = sb.reverse();
            rtnString = '-' + sb.toString();
        } else {
            sb.append(intString);
            sb = sb.reverse();
            rtnString = sb.toString();
        }
        
        try {
            return Integer.parseInt(rtnString);
        } catch (NumberFormatException e) {
            return 0;
        }
        
    }
}
