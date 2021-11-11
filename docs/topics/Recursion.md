<!-- omit in toc -->
# Recursion

- [Problems](#problems)
- [Statistics](#statistics)

## Problems

| # | Title | Solution | Difficulty | Topics | Doc |
|:----:|:----:|:----:|:----:|:----:|:----:|
| [<span id="problem-50">50</span>](#problem-50 "#50") | [Pow(x, n)](https://leetcode-cn.com/problems/powx-n/ "https://leetcode-cn.com/problems/powx-n/") | [Java](../../java/src/50.%20Powxn.java "java/src/50.%20Powxn.java") [Go](../../go/src/50.go "go/src/50.go") | Medium | `Recursion`, `Math` | [:page_facing_up:](../../docs/50.%20Pow%28x%2C%20n%29.md "docs/50.%20Pow%28x%2C%20n%29.md") |
| [<span id="problem-1137">1137</span>](#problem-1137 "#1137") | [N-th Tribonacci Number <br>第 N 个泰波那契数](https://leetcode-cn.com/problems/n-th-tribonacci-number/ "https://leetcode-cn.com/problems/n-th-tribonacci-number/") | [Java](../../java/src/1137.%20NthTribonacciNumber.java "java/src/1137.%20NthTribonacciNumber.java") | Easy | `Recursion` | [:page_facing_up:](../../docs/1137.%20N-th%20Tribonacci%20Number%20%E7%AC%AC%20N%20%E4%B8%AA%E6%B3%B0%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0.md "docs/1137.%20N-th%20Tribonacci%20Number%20%E7%AC%AC%20N%20%E4%B8%AA%E6%B3%B0%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0.md") |
| [<span id="problem-剑指-Offer-06">剑指 Offer 06</span>](#problem-剑指-Offer-06 "#剑指 Offer 06") | [从尾到头打印链表](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/ "https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/") |  [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_06.go "go/src/%E5%89%91%E6%8C%87_Offer_06.go") | Easy | `Stack`, `Recursion`, `Linked List`, `Two Pointers` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2006.%20%E4%BB%8E%E5%B0%BE%E5%88%B0%E5%A4%B4%E6%89%93%E5%8D%B0%E9%93%BE%E8%A1%A8.md "docs/%E5%89%91%E6%8C%87%20Offer%2006.%20%E4%BB%8E%E5%B0%BE%E5%88%B0%E5%A4%B4%E6%89%93%E5%8D%B0%E9%93%BE%E8%A1%A8.md") |
| [<span id="problem-剑指-Offer-16">剑指 Offer 16</span>](#problem-剑指-Offer-16 "#剑指 Offer 16") | [数值的整数次方](https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/ "https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/") |  [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_16.go "go/src/%E5%89%91%E6%8C%87_Offer_16.go") | Medium | `Recursion`, `Math` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2016.%20%E6%95%B0%E5%80%BC%E7%9A%84%E6%95%B4%E6%95%B0%E6%AC%A1%E6%96%B9.md "docs/%E5%89%91%E6%8C%87%20Offer%2016.%20%E6%95%B0%E5%80%BC%E7%9A%84%E6%95%B4%E6%95%B0%E6%AC%A1%E6%96%B9.md") |
| [<span id="problem-剑指-Offer-24">剑指 Offer 24</span>](#problem-剑指-Offer-24 "#剑指 Offer 24") | [反转链表](https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/ "https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/") |  [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_24.go "go/src/%E5%89%91%E6%8C%87_Offer_24.go") | Easy | `Recursion`, `Linked List` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2024.%20%E5%8F%8D%E8%BD%AC%E9%93%BE%E8%A1%A8.md "docs/%E5%89%91%E6%8C%87%20Offer%2024.%20%E5%8F%8D%E8%BD%AC%E9%93%BE%E8%A1%A8.md") |
| [<span id="problem-剑指-Offer-25">剑指 Offer 25</span>](#problem-剑指-Offer-25 "#剑指 Offer 25") | [合并两个排序的链表](https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/ "https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/") |  [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_25.go "go/src/%E5%89%91%E6%8C%87_Offer_25.go") | Easy | `Recursion`, `Linked List` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2025.%20%E5%90%88%E5%B9%B6%E4%B8%A4%E4%B8%AA%E6%8E%92%E5%BA%8F%E7%9A%84%E9%93%BE%E8%A1%A8.md "docs/%E5%89%91%E6%8C%87%20Offer%2025.%20%E5%90%88%E5%B9%B6%E4%B8%A4%E4%B8%AA%E6%8E%92%E5%BA%8F%E7%9A%84%E9%93%BE%E8%A1%A8.md") |
| [<span id="problem-剑指-Offer-62">剑指 Offer 62</span>](#problem-剑指-Offer-62 "#剑指 Offer 62") | [圆圈中最后剩下的数字](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/ "https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/") |  [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_62.go "go/src/%E5%89%91%E6%8C%87_Offer_62.go") | Easy | `Recursion`, `Math` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2062.%20%E5%9C%86%E5%9C%88%E4%B8%AD%E6%9C%80%E5%90%8E%E5%89%A9%E4%B8%8B%E7%9A%84%E6%95%B0%E5%AD%97.md "docs/%E5%89%91%E6%8C%87%20Offer%2062.%20%E5%9C%86%E5%9C%88%E4%B8%AD%E6%9C%80%E5%90%8E%E5%89%A9%E4%B8%8B%E7%9A%84%E6%95%B0%E5%AD%97.md") |


## Statistics

- Total solved problems : 7
- Total docs : 7

Group by solution language:
- Total solutions via Java : 2
- Total solutions via Go : 6
- Total solutions via Python3 : 0
- Total solutions via C++ : 0

Group by difficulty:
- Easy: 5
- Medium: 2
- Hard: 0