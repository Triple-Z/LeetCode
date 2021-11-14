<!-- omit in toc -->
# 剑指 Offer 20.  表示数值的字符串

- Difficulty: Medium
- Topics: `String`
- Link: https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Recursive Descent](#recursive-descent)
    - [Go](#go)
  - [Deterministic Finite Automaton (DFA)](#deterministic-finite-automaton-dfa)

## Description

请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。

**数值**（按顺序）可以分成以下几个部分：

1. 若干空格
2. 一个 **小数** 或者 **整数**
3. （可选）一个 `'e'` 或 `'E'` ，后面跟着一个 **整数**
4. 若干空格


**小数**（按顺序）可以分成以下几个部分：

1. （可选）一个符号字符（`'+'` 或 `'-'`）
2. 下述格式之一：
    1. 至少一位数字，后面跟着一个点 `'.'`
    2. 至少一位数字，后面跟着一个点 `'.'` ，后面再跟着至少一位数字
    3. 一个点 `'.'` ，后面跟着至少一位数字

**整数**（按顺序）可以分成以下几个部分：

1. （可选）一个符号字符（`'+'` 或 `'-'`）
2. 至少一位数字

部分数值列举如下：

- `["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]`


部分非数值列举如下：

- `["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]`
 

示例 1：
```
输入：s = "0"
输出：true
```
示例 2：
```
输入：s = "e"
输出：false
```
示例 3：
```
输入：s = "."
输出：false
```
示例 4：
```
输入：s = "    .1  "
输出：true
```

提示：

- `1 <= s.length <= 20`
- `s` 仅含英文字母（大写和小写），数字（`0-9`），加号 `'+'` ，减号 `'-'` ，空格 `' '` 或者点 `'.'` 。

## Solution

### Recursive Descent

学过《编译原理》的同学应该就知道，题目中的数值定义规则完全可以将其转换成 [EBNF](https://zh.wikipedia.org/wiki/%E6%89%A9%E5%B1%95%E5%B7%B4%E7%A7%91%E6%96%AF%E8%8C%83%E5%BC%8F) 的形式。这样就可以来写一个 LL(1) 的[递归下降解析器](https://zh.wikipedia.org/wiki/%E9%80%92%E5%BD%92%E4%B8%8B%E9%99%8D%E8%A7%A3%E6%9E%90%E5%99%A8)来判断字符串是否符合给出的形式。

我们可以将题目中给出的数值规则简单转换成如下 EBNF 表示：

```ebnf
number = [ space, ] ( float | integer ), [ ("e" | "E"), integer, ] [ space ];
space = [" "][ , space ];
float = float1 | float2;
float1 = [ sign, ] digits, "." [ , digits ];
float2 = [ sign, ] ".", digits;
integer = [ sign, ] digits;
sign = "+" | "-";
digits = digit [ , digit ];
digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
```

有了 EBNF 的表示，我们就能很轻松地按照 LL(1) 写出递归下降的解析器。当输入的字符串不符合要求时，我们只需要定义一个错误结果（如 `"ERROR"` 字符串），保证其肯定在后续阶段不会继续被解析即可。

该方法的本质就是一个不断“吃”字符串的有限状态自动机。最后我们只需要判断字符是否被“吃”完即可。最终字符串长度为 0 ，则说明该字符串能够被解析，表示的是合法的数值。否则，说明字符串不能被解析，表示的是非法的数值。

该方法的时间复杂度为 O(n)，空间复杂度为 O(1)。

#### Go

- 执行用时: 0 ms
- 内存消耗: 2.3 MB

```go
func isNumber(s string) bool {
    s = isSpace(s)
    
    if strings.Contains(s, ".") {
        s = isFloat(s)
    } else {
        s = isInteger(s)
    }

    if len(s) > 1 && (s[0] == byte('e') || s[0] == byte('E')) {
        // has 'e' or 'E'
        s = s[1:]
        s = isInteger(s)
    }

    s = isSpace(s)

    if len(s) == 0 {
        return true
    }

    return false
}

func isSpace(s string) string {
    for len(s) > 0 && s[0] == byte(' ') {
        s = s[1:]
    }
    return s
}

func isFloat(s string) string {
    s = isSign(s)
    if len(s) < 1 {
        return "ERROR"
    }
    if s[0] == byte('.') {
        s = s[1:]
        s = isDigits(s)
        return s
    }

    s = isDigits(s)
    if s[0] != byte('.') {
        return "ERROR"
    }
    s = s[1:] // eat the dot
    if len(s) > 0 && (s[0] >= byte('0') && s[0] <= byte('9')) {
        s = isDigits(s)
    }

    return s        
}

func isInteger(s string) string {
    s = isSign(s)
    s = isDigits(s)

    return s
}

func isDigits(s string) string {
    // at least one digit
    i := 0
    for len(s) > 0 && (s[0] >= byte('0') && s[0] <= byte('9')) {
        s = s[1:]
        i++
    }

    if i < 1 {
        return "ERROR"
    }
    return s
}

func isSign(s string) string {
    if len(s) > 0 && (s[0] == byte('+') || s[0] == byte('-')) {
        s = s[1:]
    }
    return s
}
```

### Deterministic Finite Automaton (DFA)

TODO：确定有限状态自动机。

https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/solution/biao-shi-shu-zhi-de-zi-fu-chuan-by-leetcode-soluti/

> 《剑指 Offer》 原书中使用的是[递归下降解析](#recursive-descent)的方法。DFA 定义状态和实现相对于递归下降来讲，并不太方便。
