<!-- omit in toc -->
# 剑指 Offer 05.  替换空格

- Difficulty: Easy
- Topics: `String`
- Link: https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Iteration](#iteration)
    - [Go](#go)

## Description

请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

 

示例 1：
```
输入：s = "We are happy."
输出："We%20are%20happy."
```

限制：
```
0 <= s 的长度 <= 10000
```


## Solution

### Iteration

遍历数组，遇到空格则替换为 `%20`，然后把 `%20` 插入到数组中。

主要考察各语言的字符串遍历方法。

#### Go

- 执行用时: 0 ms
- 内存消耗: 1.9 MB

```go
func replaceSpace(s string) string {
    b := strings.Builder{}
    for _, c := range s {
        if c == ' ' {
            b.WriteString("%20")
        } else {
            b.WriteRune(c)
        }
    }

    return b.String()
}
```
