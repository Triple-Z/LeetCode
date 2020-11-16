class Solution {
    List<int[]> vecs = Arrays.asList(new int[] { 1, 0 }, new int[] { -1, 0 }, new int[] { 0, 1 }, new int[] { 0, -1 });
    
    public boolean exist(char[][] board, String word) {
        boolean isFound = false;
        boolean[][] visited = new boolean[board.length][board[0].length];

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == word.charAt(0)) {
                    isFound = isFound || backtrack(board, word, 0, i, j, visited);
                    if (isFound) return true;
                }
            }
        }

        return isFound;
    }

    private boolean backtrack(char[][] board, String word, int curIndex, int x, int y, boolean[][] visited) {
        visited[x][y] = true;

        if (curIndex == word.length() - 1) {
            return true;
        }

        char curChar = board[x][y];
        boolean isFound = false;
        for (int[] vec : vecs) {
            int newX = x + vec[0];
            int newY = y + vec[1];

            if (newX >= 0 && newX < board.length && newY >= 0 && newY < board[0].length
                    && !visited[newX][newY] && word.charAt(curIndex + 1) == board[newX][newY]) {
                isFound = backtrack(board, word, curIndex + 1, newX, newY, visited) || isFound;
                if (isFound) break;
            }
        }
        
        visited[x][y] = false;
        return isFound;
    }
}