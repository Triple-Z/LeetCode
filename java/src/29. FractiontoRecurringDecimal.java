class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        StringBuilder sb = new StringBuilder();

        if (numerator == 0) return "0";

        long num = numerator;
        long de = denominator;

        // sign
        if (num < 0 ^ de < 0) {
            sb.append("-");
            if (num < 0) num = -num;
            if (de < 0) de = -de;
        }

        long i = num / de;
        sb.append(i);
        long re = num % de;
        if (re == 0) return sb.toString();
        sb.append('.');

        // remainder map
        Map<Long, Integer> reMap = new HashMap<>();
        while (re != 0) {
            if (reMap.containsKey(re)) {
                sb.insert(reMap.get(re), "(");
                sb.append(")");
                break;
            }
            reMap.put(re, sb.length());
            re *= 10;
            i = re / de;
            sb.append(i);
            re %= de;
        }

        return sb.toString();
    }
}