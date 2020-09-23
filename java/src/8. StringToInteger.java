class Solution {
    public int myAtoi(String str) {
        Automaton automaton = new Automaton();
        for (char c : str.toCharArray()) {
            automaton.get(c);
        }
        return (int)(automaton.sign * automaton.ans);
    }
}

class Automaton {
    public int sign = 1; // sign symbol
    public long ans = 0; // answer buffer
    private String state = "start"; // current state
    private Map<String, String[]> automatonTable = new HashMap<String, String[]>() {{
        // state -> space, +/-, number, others
        put("start", new String[]{"start", "signed", "in_number", "end"});
        put("signed", new String[]{"end", "end", "in_number", "end"});
        put("in_number", new String[]{"end", "end", "in_number", "end"});
        put("end", new String[]{"end", "end", "end", "end"});
    }};

    public void get(char c) {
        state = automatonTable.get(state)[this.get_col(c)];
        if ("in_number".equals(state)) {
            // push number
            ans = ans * 10 + (c - '0');
            ans = (sign == 1 ? Math.min(ans, (long)Integer.MAX_VALUE) : Math.min(ans, -(long)Integer.MIN_VALUE));
        } else if ("signed".equals(state)) {
            sign = (c == '+' ? 1 : -1);
        }
    }

    /**
     * Get automaton column.
     * @param c current input character.
     * @return column number for next state.
     */
    private int get_col(char c) {
        if (c == ' ') { // space 
            return 0;
        }
        if (c == '+' || c == '-') { // +/-
            return 1;
        }
        if (Character.isDigit(c)) { // number
            return 2;
        }
        return 3;
    }
}