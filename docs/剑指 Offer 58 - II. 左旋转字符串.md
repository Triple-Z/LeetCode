<!-- omit in toc -->
# 剑指 Offer 58 - II.  左旋转字符串

- Difficulty: Easy
- Topics: `Math`, `Two Pointers`, `String`
- Link: https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Twice Iteration](#twice-iteration)
    - [Go](#go)

## Description

字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。


示例 1：
```
输入: s = "abcdefg", k = 2
输出: "cdefgab"
```
示例 2：
```
输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"
```

限制：
```
1 <= k < s.length <= 10000
```


## Solution

### Twice Iteration

新建字符串，从 `[k]` 开始逐个将字符放入结果串中，再从 `[0]` 开始到 `[k-1]` ，放入结果中即可。

#### Go

- 执行用时: 0 ms
- 内存消耗: 3.6 MB

```go
func reverseLeftWords(s string, n int) string {
    b := strings.Builder{}
    for i := n; i < len(s); i++ {
        b.WriteByte(s[i])
    }
    for i := 0; i < n; i++ {
        b.WriteByte(s[i])
    }

    return b.String()
}
```
