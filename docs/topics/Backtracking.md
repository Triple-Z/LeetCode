<!-- omit in toc -->
# Backtracking

- [Problems](#problems)
- [Statistics](#statistics)

## Problems

| # | Title | Solution | Difficulty | Topics | Doc |
|:----:|:----:|:----:|:----:|:----:|:----:|
| [<span id="problem-17">17</span>](#problem-17 "#17") | [Letter Combinations of a Phone Number <br>电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/ "https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/") | [Java](../../java/src/17.%20LetterCombinationsofaPhoneNumber.java "java/src/17.%20LetterCombinationsofaPhoneNumber.java") | Medium | `String`, `Backtracking` | [:page_facing_up:](../../docs/17.%20Letter%20Combinations%20of%20a%20Phone%20Number%20%E7%94%B5%E8%AF%9D%E5%8F%B7%E7%A0%81%E7%9A%84%E5%AD%97%E6%AF%8D%E7%BB%84%E5%90%88.md "docs/17.%20Letter%20Combinations%20of%20a%20Phone%20Number%20%E7%94%B5%E8%AF%9D%E5%8F%B7%E7%A0%81%E7%9A%84%E5%AD%97%E6%AF%8D%E7%BB%84%E5%90%88.md") |
| [<span id="problem-22">22</span>](#problem-22 "#22") | [Generate Parentheses <br>括号生成](https://leetcode-cn.com/problems/generate-parentheses/ "https://leetcode-cn.com/problems/generate-parentheses/") | [Java](../../java/src/22.%20GenerateParentheses.java "java/src/22.%20GenerateParentheses.java") [Python3](../../py3/22.py "py3/22.py") | Medium | `String`, `Backtracking` | [:page_facing_up:](../../docs/22.%20Generate%20Parentheses%20%E6%8B%AC%E5%8F%B7%E7%94%9F%E6%88%90.md "docs/22.%20Generate%20Parentheses%20%E6%8B%AC%E5%8F%B7%E7%94%9F%E6%88%90.md") |
| [<span id="problem-46">46</span>](#problem-46 "#46") | [Permutations <br>全排列](https://leetcode-cn.com/problems/permutations/ "https://leetcode-cn.com/problems/permutations/") | [Java](../../java/src/46.%20Permutations.java "java/src/46.%20Permutations.java") [Python3](../../py3/46.py "py3/46.py") | Medium | `Backtracking` | [:page_facing_up:](../../docs/46.%20Permutations%20%E5%85%A8%E6%8E%92%E5%88%97.md "docs/46.%20Permutations%20%E5%85%A8%E6%8E%92%E5%88%97.md") |
| [<span id="problem-78">78</span>](#problem-78 "#78") | [Subsets <br>子集](https://leetcode-cn.com/problems/subsets/ "https://leetcode-cn.com/problems/subsets/") | [Java](../../java/src/78.%20Subsets.java "java/src/78.%20Subsets.java") | Medium | `Bit Manipulation`, `Array`, `Backtracking` | [:page_facing_up:](../../docs/78.%20Subsets%20%E5%AD%90%E9%9B%86.md "docs/78.%20Subsets%20%E5%AD%90%E9%9B%86.md") |
| [<span id="problem-79">79</span>](#problem-79 "#79") | [Word Search <br>单词搜索](https://leetcode-cn.com/problems/word-search/ "https://leetcode-cn.com/problems/word-search/") | [Java](../../java/src/79.%20WordSearch.java "java/src/79.%20WordSearch.java") [Go](../../go/src/79.go "go/src/79.go") | Medium | `Array`, `Backtracking` | [:page_facing_up:](../../docs/79.%20Word%20Search%20%E5%8D%95%E8%AF%8D%E6%90%9C%E7%B4%A2.md "docs/79.%20Word%20Search%20%E5%8D%95%E8%AF%8D%E6%90%9C%E7%B4%A2.md") |
| [<span id="problem-113">113</span>](#problem-113 "#113") | [Path Sum II <br>路径总和 II](https://leetcode-cn.com/problems/path-sum-ii/ "https://leetcode-cn.com/problems/path-sum-ii/") |  [Go](../../go/src/113.go "go/src/113.go") | Medium | `Tree`, `Depth-First Search`, `Backtracking`, `Binary Tree` | [:page_facing_up:](../../docs/113.%20Path%20Sum%20II%20%E8%B7%AF%E5%BE%84%E6%80%BB%E5%92%8C%20II.md "docs/113.%20Path%20Sum%20II%20%E8%B7%AF%E5%BE%84%E6%80%BB%E5%92%8C%20II.md") |
| [<span id="problem-剑指-Offer-12">剑指 Offer 12</span>](#problem-剑指-Offer-12 "#剑指 Offer 12") | [矩阵中的路径](https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/ "https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/") |  [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_12.go "go/src/%E5%89%91%E6%8C%87_Offer_12.go") | Medium | `Array`, `Backtracking`, `Matrix` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2012.%20%E7%9F%A9%E9%98%B5%E4%B8%AD%E7%9A%84%E8%B7%AF%E5%BE%84.md "docs/%E5%89%91%E6%8C%87%20Offer%2012.%20%E7%9F%A9%E9%98%B5%E4%B8%AD%E7%9A%84%E8%B7%AF%E5%BE%84.md") |
| [<span id="problem-剑指-Offer-34">剑指 Offer 34</span>](#problem-剑指-Offer-34 "#剑指 Offer 34") | [二叉树中和为某一值的路径](https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/ "https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/") |  [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_34.go "go/src/%E5%89%91%E6%8C%87_Offer_34.go") | Medium | `Tree`, `Depth-First Search`, `Backtracking`, `Binary Tree` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2034.%20%E4%BA%8C%E5%8F%89%E6%A0%91%E4%B8%AD%E5%92%8C%E4%B8%BA%E6%9F%90%E4%B8%80%E5%80%BC%E7%9A%84%E8%B7%AF%E5%BE%84.md "docs/%E5%89%91%E6%8C%87%20Offer%2034.%20%E4%BA%8C%E5%8F%89%E6%A0%91%E4%B8%AD%E5%92%8C%E4%B8%BA%E6%9F%90%E4%B8%80%E5%80%BC%E7%9A%84%E8%B7%AF%E5%BE%84.md") |


## Statistics

- Total solved problems : 8
- Total docs : 8

Group by solution language:
- Total solutions via Java : 5
- Total solutions via Go : 4
- Total solutions via Python3 : 2
- Total solutions via C++ : 0

Group by difficulty:
- Easy: 0
- Medium: 8
- Hard: 0