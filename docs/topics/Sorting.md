<!-- omit in toc -->
# Sorting

- [Problems](#problems)
- [Statistics](#statistics)

## Problems

| # | Title | Solution | Difficulty | Topics | Doc |
|:----:|:----:|:----:|:----:|:----:|:----:|
| [<span id="problem-217">217</span>](#problem-217 "#217") | [Contains Duplicate <br>存在重复元素](https://leetcode-cn.com/problems/contains-duplicate/ "https://leetcode-cn.com/problems/contains-duplicate/") |  [Python3](../../py3/217.py "py3/217.py") | Easy | `Array`, `Hash Table`, `Sorting` | [:page_facing_up:](../../docs/217.%20Contains%20Duplicate%20%E5%AD%98%E5%9C%A8%E9%87%8D%E5%A4%8D%E5%85%83%E7%B4%A0.md "docs/217.%20Contains%20Duplicate%20%E5%AD%98%E5%9C%A8%E9%87%8D%E5%A4%8D%E5%85%83%E7%B4%A0.md") |
| [<span id="problem-剑指-Offer-03">剑指 Offer 03</span>](#problem-剑指-Offer-03 "#剑指 Offer 03") | [数组中重复的数字](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/ "https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/") |  [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_03.go "go/src/%E5%89%91%E6%8C%87_Offer_03.go") | Easy | `Array`, `Hash Table`, `Sorting` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2003.%20%E6%95%B0%E7%BB%84%E4%B8%AD%E9%87%8D%E5%A4%8D%E7%9A%84%E6%95%B0%E5%AD%97.md "docs/%E5%89%91%E6%8C%87%20Offer%2003.%20%E6%95%B0%E7%BB%84%E4%B8%AD%E9%87%8D%E5%A4%8D%E7%9A%84%E6%95%B0%E5%AD%97.md") |
| [<span id="problem-剑指-Offer-21">剑指 Offer 21</span>](#problem-剑指-Offer-21 "#剑指 Offer 21") | [调整数组顺序使奇数位于偶数前面](https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/ "https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/") |  [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_21.go "go/src/%E5%89%91%E6%8C%87_Offer_21.go") | Easy | `Array`, `Two Pointers`, `Sorting` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2021.%20%E8%B0%83%E6%95%B4%E6%95%B0%E7%BB%84%E9%A1%BA%E5%BA%8F%E4%BD%BF%E5%A5%87%E6%95%B0%E4%BD%8D%E4%BA%8E%E5%81%B6%E6%95%B0%E5%89%8D%E9%9D%A2.md "docs/%E5%89%91%E6%8C%87%20Offer%2021.%20%E8%B0%83%E6%95%B4%E6%95%B0%E7%BB%84%E9%A1%BA%E5%BA%8F%E4%BD%BF%E5%A5%87%E6%95%B0%E4%BD%8D%E4%BA%8E%E5%81%B6%E6%95%B0%E5%89%8D%E9%9D%A2.md") |
| [<span id="problem-剑指-Offer-39">剑指 Offer 39</span>](#problem-剑指-Offer-39 "#剑指 Offer 39") | [数组中出现次数超过一半的数字](https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/ "https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/") |  [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_39.go "go/src/%E5%89%91%E6%8C%87_Offer_39.go") | Easy | `Array`, `Hash Table`, `Divide and Conquer`, `Counting`, `Sorting` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2039.%20%E6%95%B0%E7%BB%84%E4%B8%AD%E5%87%BA%E7%8E%B0%E6%AC%A1%E6%95%B0%E8%B6%85%E8%BF%87%E4%B8%80%E5%8D%8A%E7%9A%84%E6%95%B0%E5%AD%97.md "docs/%E5%89%91%E6%8C%87%20Offer%2039.%20%E6%95%B0%E7%BB%84%E4%B8%AD%E5%87%BA%E7%8E%B0%E6%AC%A1%E6%95%B0%E8%B6%85%E8%BF%87%E4%B8%80%E5%8D%8A%E7%9A%84%E6%95%B0%E5%AD%97.md") |
| [<span id="problem-剑指-Offer-40">剑指 Offer 40</span>](#problem-剑指-Offer-40 "#剑指 Offer 40") | [最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/ "https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/") |  [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_40.go "go/src/%E5%89%91%E6%8C%87_Offer_40.go") | Easy | `Array`, `Divide and Conquer`, `Quickselect`, `Sorting`, `Heap` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2040.%20%E6%9C%80%E5%B0%8F%E7%9A%84k%E4%B8%AA%E6%95%B0.md "docs/%E5%89%91%E6%8C%87%20Offer%2040.%20%E6%9C%80%E5%B0%8F%E7%9A%84k%E4%B8%AA%E6%95%B0.md") |
| [<span id="problem-剑指-Offer-45">剑指 Offer 45</span>](#problem-剑指-Offer-45 "#剑指 Offer 45") | [把数组排成最小的数](https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/ "https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/") |  [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_45.go "go/src/%E5%89%91%E6%8C%87_Offer_45.go") | Medium | `Greedy`, `String`, `Sorting` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2045.%20%E6%8A%8A%E6%95%B0%E7%BB%84%E6%8E%92%E6%88%90%E6%9C%80%E5%B0%8F%E7%9A%84%E6%95%B0.md "docs/%E5%89%91%E6%8C%87%20Offer%2045.%20%E6%8A%8A%E6%95%B0%E7%BB%84%E6%8E%92%E6%88%90%E6%9C%80%E5%B0%8F%E7%9A%84%E6%95%B0.md") |
| [<span id="problem-剑指-Offer-61">剑指 Offer 61</span>](#problem-剑指-Offer-61 "#剑指 Offer 61") | [扑克牌中的顺子](https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/ "https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/") |  [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_61.go "go/src/%E5%89%91%E6%8C%87_Offer_61.go") | Easy | `Array`, `Sorting` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2061.%20%E6%89%91%E5%85%8B%E7%89%8C%E4%B8%AD%E7%9A%84%E9%A1%BA%E5%AD%90.md "docs/%E5%89%91%E6%8C%87%20Offer%2061.%20%E6%89%91%E5%85%8B%E7%89%8C%E4%B8%AD%E7%9A%84%E9%A1%BA%E5%AD%90.md") |


## Statistics

- Total solved problems : 7
- Total docs : 7

Group by solution language:
- Total solutions via Java : 0
- Total solutions via Go : 6
- Total solutions via Python3 : 1
- Total solutions via C++ : 0

Group by difficulty:
- Easy: 6
- Medium: 1
- Hard: 0