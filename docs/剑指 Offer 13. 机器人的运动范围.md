<!-- omit in toc -->
# 剑指 Offer 13.  机器人的运动范围

- Difficulty: Medium
- Topics: `Depth-First Search`, `Breadth-First Search`, `Dynamic Programming`
- Link: https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Breadth-First Search](#breadth-first-search)
    - [Go](#go)
  - [Depth-First Search](#depth-first-search)
  - [Dynamic Programming](#dynamic-programming)
  - [Magic](#magic)

## Description

地上有一个m行n列的方格，从坐标 `[0,0]` 到坐标 `[m-1,n-1]` 。一个机器人从坐标 `[0, 0]` 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 `[35, 37]` ，因为3+5+3+7=18。但它不能进入方格 `[35, 38]`，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：
```
输入：m = 2, n = 3, k = 1
输出：3
```
示例 2：
```
输入：m = 3, n = 1, k = 0
输出：1
```
提示：

- `1 <= n,m <= 100`
- `0 <= k <= 20`


## Solution

### Breadth-First Search

此题与 [岛屿数量](./200.%20Number%20of%20Islands%20岛屿数量.md) 类似，都是根据特定条件区分格子面积。只不过这道题的条件为：合法的格子行坐标和列坐标数位之和不能大于 k 。🤖从 (0, 0) 出发，虽说是可以上下左右进行移动，但是要计算其能达到的最大面积，只需要在每个可到达的格子上再进行向右和向下两种推演即可。很明显，用广度优先遍历能够比较简单的完成这个任务。最后要注意去重的问题，借助一个辅助数组 `visited` 来做访问标识即可。遍历的过程中，取出队列首部元素，并判断其右方和下方的位置是否合法，若合法将新位置加入队列，继续遍历，直至队列为空。

由于题目中说明行坐标和列坐标不会大于 100（0~99），即最多只为两位数。因此，可以直接用 `row/10 + row%10 + col/10 + col%10` 得出行坐标和列坐标数位之和。

此方法的时间复杂度为 O(mn)，空间复杂度为 O(mn)。

#### Go

- 执行用时: 0 ms
- 内存消耗: 3.2 MB

```go
func movingCount(m int, n int, k int) int {
    queue := list.New()
    directions := [][]int{
        {0, 1},
        {1, 0},
    }
    visited := make([][]bool, m)
    for i := 0; i < m; i++ {
        visited[i] = make([]bool, n)
    }

    queue.PushBack([]int{0, 0})
    visited[0][0] = true

    ans := 0
    for queue.Len() > 0 {
        curPos := queue.Remove(queue.Front()).([]int)
        ans++
        for i := 0; i < 2; i++ {
            newX := curPos[0] + directions[i][0]
            newY := curPos[1] + directions[i][1]
            xySum := newX / 10 + newX % 10 + newY / 10 + newY % 10
            if newX >= 0 && newX < m && newY >= 0 && newY < n && !visited[newX][newY] && xySum <= k {
                queue.PushBack([]int{newX, newY})
                visited[newX][newY] = true
            }
        }
    }

    return ans
}
```

### Depth-First Search

发现 LeetCode 上的 DFS 方法普遍比 BFS 方法使用的内存更少，怀疑是堆内存和栈内存使用差异。理论上两者应该差不多，可能是只记录了堆内存使用所致。

TODO 深度优先搜索

https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/ji-qi-ren-de-yun-dong-fan-wei-by-leetcode-solution/

### Dynamic Programming

$$
dp(i, j) = max(dp(i-1, j), dp(i, j-1)) \\
s.t. \space i/10 + i\%10 + j/10 + j\%10 \le k
$$

https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/san-chong-fang-fa-ji-dui-bi-fen-xi-by-yu-rbil/

### Magic

不知道什么方法，在提交区里找到的，几乎双百。

- 执行用时: 0 ms
- 内存消耗: 1.9 MB

```go
func digitSum(nums... int) (res int) {
    for _, v := range nums {
        for v > 0 {
            res += v % 10
            v /= 10
        }
    }
    return
}

func movingCount(m int, n int, k int) (res int) {
    board := k+1
    if k >= 8 {
        board = (k - 7) * 10
    }
    for i := 0; i < m; i++ {
        for j := 0; j < n && i + j < board; j++ {
            if digitSum(i, j) <= k {
                res++
            }
        }
    }
    return res
}
```

