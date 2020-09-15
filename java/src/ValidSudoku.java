class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, Integer> row[] = new HashMap[board.length];
        Map<Integer, Integer> column[] = new HashMap[board[0].length];
        Map<Integer, Integer> boxes[] = new HashMap[9];

        for (int i = 0; i < 9; i++) {
            row[i] = new HashMap<Integer, Integer>();
            column[i] = new HashMap<Integer, Integer>();
            boxes[i] = new HashMap<Integer, Integer>();
        }

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] == '.') continue;
                
                int boxIndex = (i / 3) * 3 + j / 3;
                int num = (int) board[i][j];
                
                row[i].put(num, row[i].getOrDefault(num, 0) + 1);
                column[j].put(num, column[j].getOrDefault(num, 0) + 1);
                boxes[boxIndex].put(num, boxes[boxIndex].getOrDefault(num, 0) + 1);

                if (
                    row[i].get(num) > 1
                    || column[j].get(num) > 1
                    || boxes[boxIndex].get(num) > 1
                ) {
                    return false;
                }
            }
        }
        return true;
    }
}