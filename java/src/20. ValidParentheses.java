class Solution {
    public boolean isValid(String s) {
        Deque<Character> left = new LinkedList<>();

        Map<Character, Character> paraMap = new HashMap<>(){{
            put(')', '(');
            put('}', '{');
            put(']', '[');
        }};
        
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') left.push(c);
            else if (c == ')' || c == '}' || c == ']') {
                if (left.peek() != paraMap.get(c)) {
                    return false;
                }
                left.pop();
            }
        }

        if (!left.isEmpty()) return false;
        return true;
    }
}
