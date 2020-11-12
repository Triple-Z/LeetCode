class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> ans = new LinkedList<>();
        if (digits.length() == 0) return ans;
        Map<Character, List<String>> digitCharMap = new HashMap<>(){{
            put('2', Arrays.asList("a", "b", "c"));
            put('3', Arrays.asList("d", "e", "f"));
            put('4', Arrays.asList("g", "h", "i"));
            put('5', Arrays.asList("j", "k", "l"));
            put('6', Arrays.asList("m", "n", "o"));
            put('7', Arrays.asList("p", "q", "r", "s"));
            put('8', Arrays.asList("t", "u", "v"));
            put('9', Arrays.asList("w", "x", "y", "z"));
        }};

        backtrack(ans, digits, 0, digitCharMap, new StringBuilder());

        return ans;
    }

    private void backtrack(
        List<String> ans, String digits, int index, 
        Map<Character, List<String>> digitCharMap, 
        StringBuilder combination
    ) {
        if (index == digits.length()) {
            ans.add(combination.toString());
        } else {
            char curDigit = digits.charAt(index);
            for (String letter : digitCharMap.get(curDigit)) {
                combination.append(letter);
                backtrack(ans, digits, index+1, digitCharMap, combination);
                // backtrack
                combination.deleteCharAt(index);
            }
        }
    }
}