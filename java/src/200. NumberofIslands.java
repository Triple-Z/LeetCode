class Solution {
    public int numIslands(char[][] grid) {
        LinkedList<int[]> dotQueue = new LinkedList<>();
        int[][] vecs = new int[][]{
            {0, 1},
            {0, -1},
            {1, 0},
            {-1, 0},
        };
        int ans = 0;
        
        int m = grid.length;
        int n = grid[0].length;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    ans++;
                    // find land
                    dotQueue.addLast(new int[]{i, j});
                    // unset land
                    grid[i][j] = '0';

                    // breadth-first search
                    while (!dotQueue.isEmpty()) {
                        int[] curDot = dotQueue.pollFirst();
                        for (int[] vec : vecs) {
                            int x = curDot[0] + vec[0];
                            int y = curDot[1] + vec[1];

                            if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] == '1') {
                                dotQueue.addLast(new int[]{x, y});
                                grid[x][y] = '0';
                            }
                        }
                    }
                }
            }
        }

        return ans;
    }
}