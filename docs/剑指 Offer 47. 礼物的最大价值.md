<!-- omit in toc -->
# 剑指 Offer 47.  礼物的最大价值

- Difficulty: Medium
- Topics: `Array`, `Dynamic Programming`, `Matrix`
- Link: https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Dynamic Programming](#dynamic-programming)
    - [Go](#go)

## Description

在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

 

示例 1:
```
输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
```

提示：

- `0 < grid.length <= 200`
- `0 < grid[0].length <= 200`


## Solution

### Dynamic Programming

首先，拿礼物的起点一定是棋盘左上角，终点则为棋盘右下角，且每次只能做以下两个动作的其中一个：
1. 向右移动一格，拿取右边格子的礼物。
2. 向下移动一格，拿取下边格子的礼物。

对于某个特定位置的格子来说，此处能够获取到的累计最高价值的礼物，即为左边格子和上方格子能获取到的累计最高价值礼物的最大值，与自身格子上礼物价值之和。因此，我们可以通过顺序计算之前格子各自能获得的最大礼物价值，从而确定出终点可获得的最大值。

那么我们就可以用动态规划通过缓存子问题的结果，来计算出最终的答案。

此题的递推方程也很容易就能够得出，如下：
$$
dp(i, j) = \begin{cases}
	MAX(dp(i-1, j), dp(j, j-1)) + grid(i-1, j-1), & i \ge 1 \text{ and } j \ge 1 \\
	0, & i = 0 \text{ or } j = 0
\end{cases}
$$

此题可以通过申请一个 `(m+1) * (n+1)` 大小的 dp 数组，来规避边界情况的处理。也可以先将最上行和最左列优先赋值（前缀和），再计算 `(1, 1) -> (m-1, n-1)` 的结果。

#### Go

申请一个 `(m+1) * (n+1)` 大小的 dp 数组。

- 执行用时: 4 ms
- 内存消耗: 4.3 MB

```go
func maxValue(grid [][]int) int {
    m := len(grid)
    if m == 0 {
        return 0
    }
    n := len(grid[0])
    if n == 0 {
        return 0
    }

    var dp [][]int = make([][]int, m+1)  // (m+1)*(n+1)
    for i := 0; i < m+1; i++ {
        dp[i] = make([]int, n+1)
    }

    for i := 1; i <= m; i++ {
        for j := 1; j <= n; j++ {
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
        }
    }

    return dp[m][n]
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```

先将最上行和最左列优先赋值（前缀和），再计算 `(1, 1) -> (m-1, n-1)` 的结果。

- 执行用时: 4 ms
- 内存消耗: 4.3 MB

```go
func maxValue(grid [][]int) int {
    m := len(grid)
    if m == 0 {
        return 0
    }
    n := len(grid[0])
    if n == 0 {
        return 0
    }

    var dp [][]int = make([][]int, m)
    for i := 0; i < m; i++ {
        dp[i] = make([]int, n)
    }

    jSum := 0
    for j := 0; j < n; j++ {
        jSum += grid[0][j]
        dp[0][j] = jSum
    }

    iSum := 0
    for i := 0; i < m; i++ {
        iSum += grid[i][0]
        dp[i][0] = iSum
    }

    for i := 1; i < m; i++ {
        for j := 1; j < n; j++ {
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        }
    }

    return dp[m-1][n-1]
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```