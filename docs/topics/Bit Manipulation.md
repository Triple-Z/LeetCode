<!-- omit in toc -->
# Bit Manipulation

- [Problems](#problems)
- [Statistics](#statistics)

## Problems

| # | Title | Solution | Difficulty | Topics | Doc |
|:----:|:----:|:----:|:----:|:----:|:----:|
| [<span id="problem-78">78</span>](#problem-78 "#78") | [Subsets <br>子集](https://leetcode-cn.com/problems/subsets/ "https://leetcode-cn.com/problems/subsets/") | [Java](../../java/src/78.%20Subsets.java "java/src/78.%20Subsets.java") | Medium | `Bit Manipulation`, `Array`, `Backtracking` | [:page_facing_up:](../../docs/78.%20Subsets%20%E5%AD%90%E9%9B%86.md "docs/78.%20Subsets%20%E5%AD%90%E9%9B%86.md") |
| [<span id="problem-136">136</span>](#problem-136 "#136") | [Single Number <br>只出现一次的数字](https://leetcode-cn.com/problems/single-number/ "https://leetcode-cn.com/problems/single-number/") |  [Go](../../go/src/136.go "go/src/136.go") [Python3](../../py3/136.py "py3/136.py") | Easy | `Bit Manipulation`, `Hash Table` | [:page_facing_up:](../../docs/136.%20Single%20Number%20%E5%8F%AA%E5%87%BA%E7%8E%B0%E4%B8%80%E6%AC%A1%E7%9A%84%E6%95%B0%E5%AD%97.md "docs/136.%20Single%20Number%20%E5%8F%AA%E5%87%BA%E7%8E%B0%E4%B8%80%E6%AC%A1%E7%9A%84%E6%95%B0%E5%AD%97.md") |
| [<span id="problem-169">169</span>](#problem-169 "#169") | [Majority Element <br>多数元素](https://leetcode-cn.com/problems/majority-element/ "https://leetcode-cn.com/problems/majority-element/") | [Java](../../java/src/169.%20MajorityElement.java "java/src/169.%20MajorityElement.java") [Python3](../../py3/169.py "py3/169.py") | Easy | `Bit Manipulation`, `Array`, `Divide and Conquer` | [:page_facing_up:](../../docs/169.%20Majority%20Element%20%E5%A4%9A%E6%95%B0%E5%85%83%E7%B4%A0.md "docs/169.%20Majority%20Element%20%E5%A4%9A%E6%95%B0%E5%85%83%E7%B4%A0.md") |
| [<span id="problem-190">190</span>](#problem-190 "#190") | [Reverse Bits <br>颠倒二进制位](https://leetcode-cn.com/problems/reverse-bits/description/ "https://leetcode-cn.com/problems/reverse-bits/description/") | [Java](../../java/src/190.%20ReverseBits.java "java/src/190.%20ReverseBits.java") | Easy | `Bit Manipulation` | [:page_facing_up:](../../docs/190.%20Reverse%20Bits%20%E9%A2%A0%E5%80%92%E4%BA%8C%E8%BF%9B%E5%88%B6%E4%BD%8D.md "docs/190.%20Reverse%20Bits%20%E9%A2%A0%E5%80%92%E4%BA%8C%E8%BF%9B%E5%88%B6%E4%BD%8D.md") |
| [<span id="problem-191">191</span>](#problem-191 "#191") | [Number of 1 Bits <br>位1的个数](https://leetcode-cn.com/problems/number-of-1-bits/ "https://leetcode-cn.com/problems/number-of-1-bits/") | [Java](../../java/src/191.%20Numberof1Bits.java "java/src/191.%20Numberof1Bits.java") | Easy | `Bit Manipulation` | [:page_facing_up:](../../docs/191.%20Number%20of%201%20Bits%20%E4%BD%8D1%E7%9A%84%E4%B8%AA%E6%95%B0.md "docs/191.%20Number%20of%201%20Bits%20%E4%BD%8D1%E7%9A%84%E4%B8%AA%E6%95%B0.md") |
| [<span id="problem-268">268</span>](#problem-268 "#268") | [Missing Number <br>缺失数字](https://leetcode-cn.com/problems/missing-number/ "https://leetcode-cn.com/problems/missing-number/") | [Java](../../java/src/268.%20MissingNumber.java "java/src/268.%20MissingNumber.java") | Easy | `Bit Manipulation`, `Array`, `Math` | [:page_facing_up:](../../docs/268.%20Missing%20Number%20%E7%BC%BA%E5%A4%B1%E6%95%B0%E5%AD%97.md "docs/268.%20Missing%20Number%20%E7%BC%BA%E5%A4%B1%E6%95%B0%E5%AD%97.md") |
| [<span id="problem-371">371</span>](#problem-371 "#371") | [Sum of Two Integers <br>两整数之和](https://leetcode-cn.com/problems/sum-of-two-integers/ "https://leetcode-cn.com/problems/sum-of-two-integers/") | [Java](../../java/src/371.%20SumofTwoIntegers.java "java/src/371.%20SumofTwoIntegers.java") | Easy | `Bit Manipulation` | [:page_facing_up:](../../docs/371.%20Sum%20of%20Two%20Integers%20%E4%B8%A4%E6%95%B4%E6%95%B0%E4%B9%8B%E5%92%8C.md "docs/371.%20Sum%20of%20Two%20Integers%20%E4%B8%A4%E6%95%B4%E6%95%B0%E4%B9%8B%E5%92%8C.md") |
| [<span id="problem-461">461</span>](#problem-461 "#461") | [Hamming Distance <br>汉明距离](https://leetcode-cn.com/problems/hamming-distance/ "https://leetcode-cn.com/problems/hamming-distance/") | [Java](../../java/src/461.%20HammingDistance.java "java/src/461.%20HammingDistance.java") [Python3](../../py3/461.py "py3/461.py") | Easy | `Bit Manipulation` | [:page_facing_up:](../../docs/461.%20Hamming%20Distance%20%E6%B1%89%E6%98%8E%E8%B7%9D%E7%A6%BB.md "docs/461.%20Hamming%20Distance%20%E6%B1%89%E6%98%8E%E8%B7%9D%E7%A6%BB.md") |
| [<span id="problem-剑指-Offer-15">剑指 Offer 15</span>](#problem-剑指-Offer-15 "#剑指 Offer 15") | [二进制中1的个数](https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/ "https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/") |  [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_15.go "go/src/%E5%89%91%E6%8C%87_Offer_15.go") | Easy | `Bit Manipulation` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2015.%20%E4%BA%8C%E8%BF%9B%E5%88%B6%E4%B8%AD1%E7%9A%84%E4%B8%AA%E6%95%B0.md "docs/%E5%89%91%E6%8C%87%20Offer%2015.%20%E4%BA%8C%E8%BF%9B%E5%88%B6%E4%B8%AD1%E7%9A%84%E4%B8%AA%E6%95%B0.md") |
| [<span id="problem-剑指-Offer-53---II">剑指 Offer 53 - II</span>](#problem-剑指-Offer-53---II "#剑指 Offer 53 - II") | [0<br>～n-1中缺失的数字](https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/ "https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/") |  [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_53_-_II.go "go/src/%E5%89%91%E6%8C%87_Offer_53_-_II.go") | Easy | `Bit Manipulation`, `Array`, `Hash Table`, `Math`, `Binary Search` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2053%20-%20II.%200%EF%BD%9En-1%E4%B8%AD%E7%BC%BA%E5%A4%B1%E7%9A%84%E6%95%B0%E5%AD%97.md "docs/%E5%89%91%E6%8C%87%20Offer%2053%20-%20II.%200%EF%BD%9En-1%E4%B8%AD%E7%BC%BA%E5%A4%B1%E7%9A%84%E6%95%B0%E5%AD%97.md") |
| [<span id="problem-剑指-Offer-65">剑指 Offer 65</span>](#problem-剑指-Offer-65 "#剑指 Offer 65") | [不用加减乘除做加法](https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/ "https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/") |  [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_65.go "go/src/%E5%89%91%E6%8C%87_Offer_65.go") | Easy | `Bit Manipulation`, `Math` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2065.%20%E4%B8%8D%E7%94%A8%E5%8A%A0%E5%87%8F%E4%B9%98%E9%99%A4%E5%81%9A%E5%8A%A0%E6%B3%95.md "docs/%E5%89%91%E6%8C%87%20Offer%2065.%20%E4%B8%8D%E7%94%A8%E5%8A%A0%E5%87%8F%E4%B9%98%E9%99%A4%E5%81%9A%E5%8A%A0%E6%B3%95.md") |


## Statistics

- Total solved problems : 11
- Total docs : 11

Group by solution language:
- Total solutions via Java : 7
- Total solutions via Go : 4
- Total solutions via Python3 : 3
- Total solutions via C++ : 0

Group by difficulty:
- Easy: 10
- Medium: 1
- Hard: 0