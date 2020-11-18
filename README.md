<!-- omit in toc -->
# LeetCode

LeetCode 练习仓库。

> Last updated: 2020-11-18 13:56:43.202297 UTC
>
> Run `make update` to update this file, or just make a Git commit (if the `pre-commit` hooks are installed).

- [Problems](#problems)
- [Statistics](#statistics)
- [License](#license)

## Problems

| # | Title | Solution | Difficulty | Topics | Doc |
|:----:|:----:|:----:|:----:|:----:|:----:|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | [Java](java/src/1.%20TwoSum.java) [Python3](py3/1.py) [C++](cpp/src/1.cpp) | Easy | `Array`, `Hash Table` | [:page_facing_up:](docs/1.%20Two%20Sum.md) |
| 2 | [Add Two Numbers<br> 两数相加](https://leetcode-cn.com/problems/add-two-numbers/description/) | [Java](java/src/2.%20AddTwoNumbers.java) [Python3](py3/2.py) | Medium | `Linked List`, `Math` | [:page_facing_up:](docs/2.%20Add%20Two%20Numbers%20%E4%B8%A4%E6%95%B0%E7%9B%B8%E5%8A%A0.md) |
| 3 | [Longest Substring Without Repeating Characters<br> 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters) | [Java](java/src/3.%20LongestSubstringWithoutRepeatingCharacters.java) [Python3](py3/3.py) | Medium | `Hash Table`, `Two Pointers`, `String`, `Sliding Window` | [:page_facing_up:](docs/3.%20Longest%20Substring%20Without%20Repeating%20Characters%20%E6%97%A0%E9%87%8D%E5%A4%8D%E5%AD%97%E7%AC%A6%E7%9A%84%E6%9C%80%E9%95%BF%E5%AD%90%E4%B8%B2.md) |
| 4 |  |  [Python3](py3/4.py) |  |  |  |
| 5 | [Longest Palindromic Substring<br> 最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/) | [Java](java/src/5.%20LongestPalindromicSubstring.java) [Python3](py3/5.py) | Medium | `String`, `Dynamic Programming` | [:page_facing_up:](docs/5.%20Longest%20Palindromic%20Substring%20%E6%9C%80%E9%95%BF%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2.md) |
| 6 |  |  [Python3](py3/6.py) |  |  |  |
| 7 | [Reverse Integer<br> 整数反转](https://leetcode-cn.com/problems/reverse-integer/) | [Java](java/src/7.%20ReverseInteger.java) [Python3](py3/7.py) | Easy | `Math` | [:page_facing_up:](docs/7.%20Reverse%20Integer%20%E6%95%B4%E6%95%B0%E5%8F%8D%E8%BD%AC.md) |
| 8 | [String to Integer<br> 字符串转换整数(atoi)](https://leetcode-cn.com/problems/string-to-integer-atoi/) | [Java](java/src/8.%20StringToInteger.java) | Medium | `Math`, `String` | [:page_facing_up:](docs/8.%20String%20to%20Integer%20%E5%AD%97%E7%AC%A6%E4%B8%B2%E8%BD%AC%E6%8D%A2%E6%95%B4%E6%95%B0%28atoi%29.md) |
| 9 |  |  [Python3](py3/9.py) |  |  |  |
| 10 |  |  [Python3](py3/10.py) |  |  |  |
| 11 | [Container With Most Water<br> 盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water/) | [Java](java/src/11.%20ContainerWithMostWater.java) [C++](cpp/src/11.cpp) | Medium | `Array`, `Two Pointers` | [:page_facing_up:](docs/11.%20Container%20With%20Most%20Water%20%E7%9B%9B%E6%9C%80%E5%A4%9A%E6%B0%B4%E7%9A%84%E5%AE%B9%E5%99%A8.md) |
| 13 | [Roman to Integer<br> 罗马数字转整数](https://leetcode-cn.com/problems/roman-to-integer/) | [Java](java/src/13.%20RomantoInteger.java) [Python3](py3/13.py) | Easy | `Math`, `String` | [:page_facing_up:](docs/13.%20Roman%20to%20Integer%20%E7%BD%97%E9%A9%AC%E6%95%B0%E5%AD%97%E8%BD%AC%E6%95%B4%E6%95%B0.md) |
| 14 | [Longest Common Prefix<br> 最长公共前缀](https://leetcode-cn.com/problems/longest-common-prefix/) | [Java](java/src/14.%20LongestCommonPrefix.java) [Python3](py3/14.py) | Easy | `String` | [:page_facing_up:](docs/14.%20Longest%20Common%20Prefix%20%E6%9C%80%E9%95%BF%E5%85%AC%E5%85%B1%E5%89%8D%E7%BC%80.md) |
| 15 | [3Sum<br> 三数之和](https://leetcode-cn.com/problems/3sum/) | [Java](java/src/15.%203Sum.java) [C++](cpp/src/15.cpp) | Medium | `Array`, `Two Pointers` | [:page_facing_up:](docs/15.%203Sum%20%E4%B8%89%E6%95%B0%E4%B9%8B%E5%92%8C.md) |
| 16 | [3Sum Closest](https://leetcode.com/problems/3sum-closest/) |  [C++](cpp/src/16.cpp) | Medium | `Array`, `Two Pointers` | [:page_facing_up:](docs/16.%203Sum%20Closest.md) |
| 17 | [Letter Combinations of a Phone Number<br> 电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/) | [Java](java/src/17.%20LetterCombinationsofaPhoneNumber.java) | Medium | `String`, `Backtracking` | [:page_facing_up:](docs/17.%20Letter%20Combinations%20of%20a%20Phone%20Number%20%E7%94%B5%E8%AF%9D%E5%8F%B7%E7%A0%81%E7%9A%84%E5%AD%97%E6%AF%8D%E7%BB%84%E5%90%88.md) |
| 18 | [4Sum](https://leetcode.com/problems/4sum/) |  [C++](cpp/src/18.cpp) | Medium | `Array`, `Hash Table`, `Two Pointers` | [:page_facing_up:](docs/18.%204Sum.md) |
| 19 | [Remove Nth Node From End of List<br> 删除链表的倒数第N个节点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/) | [Java](java/src/19.%20RemoveNthNodeFromEndOfList.java) | Medium | `Linked List`, `Two Pointers` | [:page_facing_up:](docs/19.%20Remove%20Nth%20Node%20From%20End%20of%20List%20%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E7%9A%84%E5%80%92%E6%95%B0%E7%AC%ACN%E4%B8%AA%E8%8A%82%E7%82%B9.md) |
| 20 | [Valid Parentheses<br> 有效的括号](https://leetcode-cn.com/problems/valid-parentheses/) | [Java](java/src/20.%20ValidParentheses.java) [Python3](py3/20.py) | Easy | `Stack`, `String` | [:page_facing_up:](docs/20.%20Valid%20Parentheses%20%E6%9C%89%E6%95%88%E7%9A%84%E6%8B%AC%E5%8F%B7.md) |
| 21 | [Merge Two Sorted Lists<br> 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/) | [Java](java/src/21.%20MergeTwoSortedLists.java) [Python3](py3/21.py) | Easy | `Linked List` | [:page_facing_up:](docs/21.%20Merge%20Two%20Sorted%20Lists%20%E5%90%88%E5%B9%B6%E4%B8%A4%E4%B8%AA%E6%9C%89%E5%BA%8F%E9%93%BE%E8%A1%A8.md) |
| 22 | [Generate Parentheses<br> 括号生成](https://leetcode-cn.com/problems/generate-parentheses/) | [Java](java/src/22.%20GenerateParentheses.java) [Python3](py3/22.py) | Medium | `String`, `Backtracking` | [:page_facing_up:](docs/22.%20Generate%20Parentheses%20%E6%8B%AC%E5%8F%B7%E7%94%9F%E6%88%90.md) |
| 26 | [Remove Duplicates from Sorted Array<br> 删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/) | [Java](java/src/26.%20RemoveDuplicatesfromSortedArray.java) [C++](cpp/src/26.cpp) | Easy | `Array`, `Two Pointers` | [:page_facing_up:](docs/26.%20Remove%20Duplicates%20from%20Sorted%20Array%20%E5%88%A0%E9%99%A4%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84%E4%B8%AD%E7%9A%84%E9%87%8D%E5%A4%8D%E9%A1%B9.md) |
| 27 | [Remove Element](https://leetcode.com/problems/remove-element/) |  [C++](cpp/src/27.cpp) | Easy | `Array`, `Two Pointers` | [:page_facing_up:](docs/27.%20Remove%20Element.md) |
| 28 | [Implement strStr()<br> 实现 strStr()](https://leetcode-cn.com/problems/implement-strstr/) | [Java](java/src/28.%20ImplementstrStr.java) | Easy | `Two Pointers`, `String` | [:page_facing_up:](docs/28.%20Implement%20strStr%28%29%20%E5%AE%9E%E7%8E%B0%20strStr%28%29.md) |
| 35 | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | [Java](java/src/35.%20SearchInsertPosition.java) [Python3](py3/35.py) [C++](cpp/src/35.cpp) | Easy | `Array`, `Binary Search` | [:page_facing_up:](docs/35.%20Search%20Insert%20Position.md) |
| 36 | [Valid Sudoku<br> 有效的数独](https://leetcode-cn.com/problems/valid-sudoku/) | [Java](java/src/36.%20ValidSudoku.java) | Medium | `Hash Table` | [:page_facing_up:](docs/36.%20Valid%20Sudoku%20%E6%9C%89%E6%95%88%E7%9A%84%E6%95%B0%E7%8B%AC.md) |
| 38 | [Count and Say<br> 外观数列](https://leetcode-cn.com/problems/count-and-say/) | [Java](java/src/38.%20CountAndSay.java) | Easy | `String` | [:page_facing_up:](docs/38.%20Count%20and%20Say%20%E5%A4%96%E8%A7%82%E6%95%B0%E5%88%97.md) |
| 46 | [Permutations<br> 全排列](https://leetcode-cn.com/problems/permutations/) | [Java](java/src/46.%20Permutations.java) [Python3](py3/46.py) | Medium | `Backtracking` | [:page_facing_up:](docs/46.%20Permutations%20%E5%85%A8%E6%8E%92%E5%88%97.md) |
| 48 | [Rotate Image<br> 旋转图像](https://leetcode-cn.com/problems/rotate-image/) | [Java](java/src/48.%20RotateImage.java) | Medium | `Array` | [:page_facing_up:](docs/48.%20Rotate%20Image%20%E6%97%8B%E8%BD%AC%E5%9B%BE%E5%83%8F.md) |
| 49 | [Group Anagrams<br> 字母异位词分组](https://leetcode-cn.com/problems/group-anagrams/) | [Java](java/src/49.%20GroupAnagrams.java) | Medium | `Hash Table`, `String` | [:page_facing_up:](docs/49.%20Group%20Anagrams%20%E5%AD%97%E6%AF%8D%E5%BC%82%E4%BD%8D%E8%AF%8D%E5%88%86%E7%BB%84.md) |
| 53 | [Maximum Subarray<br> 最大子序和](https://leetcode-cn.com/problems/maximum-subarray/description/) | [Java](java/src/53.%20MaximumSubarray.java) [Python3](py3/53.py) [C++](cpp/src/53.cpp) | Easy | `Array`, `Divide and Conquer`, `Dynamic Programming` | [:page_facing_up:](docs/53.%20Maximum%20Subarray%20%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%92%8C.md) |
| 66 | [Plus One](https://leetcode.com/problems/plus-one/) |  [Python3](py3/66.py) [C++](cpp/src/66.cpp) | Easy | `Array`, `Math` | [:page_facing_up:](docs/66.%20Plus%20One.md) |
| 67 |  |  [Python3](py3/67.py) |  |  |  |
| 69 |  |  [Python3](py3/69.py) |  |  |  |
| 70 | [Climbing Stairs<br> 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/description/) | [Java](java/src/70.%20ClimbingStairs.java) [Python3](py3/70.py) | Easy | `Dynamic Programming` | [:page_facing_up:](docs/70.%20Climbing%20Stairs%20%E7%88%AC%E6%A5%BC%E6%A2%AF.md) |
| 73 | [Set Matrix Zeroes<br> 矩阵置零](https://leetcode-cn.com/problems/set-matrix-zeroes/description/) | [Java](java/src/73.%20SetMatrixZeroes.java) | Medium | `Array` | [:page_facing_up:](docs/73.%20Set%20Matrix%20Zeroes%20%E7%9F%A9%E9%98%B5%E7%BD%AE%E9%9B%B6.md) |
| 75 | [Sort Colors<br> 颜色分类](https://leetcode-cn.com/problems/sort-colors/description/) | [Java](java/src/75.%20SortColors.java) | Medium | `Sort`, `Array`, `Two Pointers` | [:page_facing_up:](docs/75.%20Sort%20Colors%20%E9%A2%9C%E8%89%B2%E5%88%86%E7%B1%BB.md) |
| 78 | [Subsets<br> 子集](https://leetcode-cn.com/problems/subsets/) | [Java](java/src/78.%20Subsets.java) | Medium | `Bit Manipulation`, `Array`, `Backtracking` | [:page_facing_up:](docs/78.%20Subsets%20%E5%AD%90%E9%9B%86.md) |
| 79 | [Word Search<br> 单词搜索](https://leetcode-cn.com/problems/word-search/) | [Java](java/src/79.%20WordSearch.java) | Medium | `Array`, `Backtracking` | [:page_facing_up:](docs/79.%20Word%20Search%20%E5%8D%95%E8%AF%8D%E6%90%9C%E7%B4%A2.md) |
| 80 | [Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) |  [C++](cpp/src/80.cpp) | Medium | `Array`, `Two Pointers` | [:page_facing_up:](docs/80.%20Remove%20Duplicates%20from%20Sorted%20Array%20II.md) |
| 88 | [Merge Sorted Array<br> 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/) | [Java](java/src/88.%20MergeSortedArray.java) [C++](cpp/src/88.cpp) | Easy | `Array`, `Two Pointers` | [:page_facing_up:](docs/88.%20Merge%20Sorted%20Array%20%E5%90%88%E5%B9%B6%E4%B8%A4%E4%B8%AA%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84.md) |
| 94 | [Binary Tree Inorder Traversal<br> 二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/) | [Java](java/src/94.%20BinaryTreeInorderTraversal.java) [Python3](py3/94.py) | Medium | `Hash Table`, `Stack`, `Tree` | [:page_facing_up:](docs/94.%20Binary%20Tree%20Inorder%20Traversal%20%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E4%B8%AD%E5%BA%8F%E9%81%8D%E5%8E%86.md) |
| 98 | [Valid Binary Search Tree<br> 验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree/) | [Java](java/src/98.%20ValidBinarySearchTree.java) | Medium | `Tree`, `Depth-first Search` | [:page_facing_up:](docs/98.%20Valid%20Binary%20Search%20Tree%20%E9%AA%8C%E8%AF%81%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.md) |
| 100 |  |  [Python3](py3/100.py) |  |  |  |
| 101 | [Symmetric Tree<br> 对称二叉树](https://leetcode-cn.com/problems/symmetric-tree/) | [Java](java/src/101.%20SymmetricTree.java) [Python3](py3/101.py) | Easy | `Tree`, `Depth-first Search`, `Breadth-first Search` | [:page_facing_up:](docs/101.%20Symmetric%20Tree%20%E5%AF%B9%E7%A7%B0%E4%BA%8C%E5%8F%89%E6%A0%91.md) |
| 102 | [Binary Tree Level Order Traversal<br> 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/) | [Java](java/src/102.%20BinaryTreeLevelOrderTraversal.java) | Medium | `Tree`, `Breadth-first Search` | [:page_facing_up:](docs/102.%20Binary%20Tree%20Level%20Order%20Traversal%20%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%82%E5%BA%8F%E9%81%8D%E5%8E%86.md) |
| 103 | [Binary Tree Zigzag Level Order Traversal<br> 二叉树的锯齿形层次遍历](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/) | [Java](java/src/103.%20BinaryTreeZigzagLevelOrderTraversal.java) | Medium | `Stack`, `Tree`, `Breadth-first Search` | [:page_facing_up:](docs/103.%20Binary%20Tree%20Zigzag%20Level%20Order%20Traversal%20%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E9%94%AF%E9%BD%BF%E5%BD%A2%E5%B1%82%E6%AC%A1%E9%81%8D%E5%8E%86.md) |
| 104 | [Maximum Depth of Binary Tree<br> 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/) | [Java](java/src/104.%20MaximumDepthOfBinaryTree.java) [Python3](py3/104.py) | Easy | `Tree`, `Depth-first Search` | [:page_facing_up:](docs/104.%20Maximum%20Depth%20of%20Binary%20Tree%20%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%A4%A7%E6%B7%B1%E5%BA%A6.md) |
| 105 | [Construct Binary Tree from Preorder and Inorder Traversal<br> 从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | [Java](java/src/105.%20ConstructBinaryTreefromPreorderandInorderTraversal.java) | Medium | `Array`, `Tree`, `Depth-first Search` | [:page_facing_up:](docs/105.%20Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal%20%E4%BB%8E%E5%89%8D%E5%BA%8F%E4%B8%8E%E4%B8%AD%E5%BA%8F%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97%E6%9E%84%E9%80%A0%E4%BA%8C%E5%8F%89%E6%A0%91.md) |
| 108 | [Convert Sorted Array to Binary Search Tree<br> 将有序数组转换为二叉树](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/) | [Java](java/src/108.%20ConvertSortedArrayToBinarySearchTree.java) | Easy | `Tree`, `Depth-first Search` | [:page_facing_up:](docs/108.%20Convert%20Sorted%20Array%20to%20Binary%20Search%20Tree%20%E5%B0%86%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E8%BD%AC%E6%8D%A2%E4%B8%BA%E4%BA%8C%E5%8F%89%E6%A0%91.md) |
| 116 | [Populating Next Right Pointers in Each Node<br> 填充每个节点的下一个右侧节点指针](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/) | [Java](java/src/116.%20PopulatingNextRightPointersinEachNode.java) | Medium | `Tree`, `Depth-first Search` | [:page_facing_up:](docs/116.%20Populating%20Next%20Right%20Pointers%20in%20Each%20Node%20%E5%A1%AB%E5%85%85%E6%AF%8F%E4%B8%AA%E8%8A%82%E7%82%B9%E7%9A%84%E4%B8%8B%E4%B8%80%E4%B8%AA%E5%8F%B3%E4%BE%A7%E8%8A%82%E7%82%B9%E6%8C%87%E9%92%88.md) |
| 118 | [Pascal's Triangle<br> 杨辉三角](https://leetcode-cn.com/problems/pascals-triangle/description/) | [Java](java/src/118.%20PascalsTriangle.java) | Easy | `Array` | [:page_facing_up:](docs/118.%20Pascal%27s%20Triangle%20%E6%9D%A8%E8%BE%89%E4%B8%89%E8%A7%92.md) |
| 121 | [Best Time to Buy and Sell Stock<br> 买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/) | [Java](java/src/121.%20BestTimetoBuyandSellStock.java) [Python3](py3/121.py) [C++](cpp/src/121.cpp) | Easy | `Array`, `Dynamic Programming` | [:page_facing_up:](docs/121.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock%20%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BA.md) |
| 122 | [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) |  [C++](cpp/src/122.cpp) | Easy | `Array`, `Greedy` | [:page_facing_up:](docs/122.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock%20II.md) |
| 123 | [Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii) |  [C++](cpp/src/123.cpp) | Hard | `Array`, `Dynamic Programming` | [:page_facing_up:](docs/123.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock%20III.md) |
| 125 | [Valid PalinDrome<br> 验证回文串](https://leetcode-cn.com/problems/valid-palindrome/) | [Java](java/src/125.%20ValidPaliDrome.java) | Easy | `Two Pointers`, `String` | [:page_facing_up:](docs/125.%20Valid%20PalinDrome%20%E9%AA%8C%E8%AF%81%E5%9B%9E%E6%96%87%E4%B8%B2.md) |
| 136 |  |  [Python3](py3/136.py) |  |  |  |
| 141 | [Linked List Cycle<br> 环形链表](https://leetcode-cn.com/problems/linked-list-cycle/) | [Java](java/src/141.%20LinkedListCycle.java) [Python3](py3/141.py) | Easy | `Linked List`, `Two Pointers` | [:page_facing_up:](docs/141.%20Linked%20List%20Cycle%20%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8.md) |
| 144 | [Binary Tree Preorder Traversal<br> 二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/) | [Java](java/src/144.%20BinaryTreePreorderTraversal.java) | Medium | `Stack`, `Tree` | [:page_facing_up:](docs/144.%20Binary%20Tree%20Preorder%20Traversal%20%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%89%8D%E5%BA%8F%E9%81%8D%E5%8E%86.md) |
| 155 | [Min Stack<br> 最小栈](https://leetcode-cn.com/problems/min-stack/) | [Java](java/src/155.%20MinStack.java) [Python3](py3/155.py) | Easy | `Stack`, `Design` | [:page_facing_up:](docs/155.%20Min%20Stack%20%E6%9C%80%E5%B0%8F%E6%A0%88.md) |
| 160 | [Intersection of Two Linked Lists<br> 相交链表](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/) | [Java](java/src/160.%20IntersectionofTwoLinkedLists.java) [Python3](py3/160.py) | Easy | `Linked List` | [:page_facing_up:](docs/160.%20Intersection%20of%20Two%20Linked%20Lists%20%E7%9B%B8%E4%BA%A4%E9%93%BE%E8%A1%A8.md) |
| 169 |  |  [Python3](py3/169.py) |  |  |  |
| 190 | [Reverse Bits<br> 颠倒二进制位](https://leetcode-cn.com/problems/reverse-bits/description/) | [Java](java/src/190.%20ReverseBits.java) | Easy | `Bit Manipulation` | [:page_facing_up:](docs/190.%20Reverse%20Bits%20%E9%A2%A0%E5%80%92%E4%BA%8C%E8%BF%9B%E5%88%B6%E4%BD%8D.md) |
| 191 | [Number of 1 Bits<br> 位1的个数](https://leetcode-cn.com/problems/number-of-1-bits/) | [Java](java/src/191.%20Numberof1Bits.java) | Easy | `Bit Manipulation` | [:page_facing_up:](docs/191.%20Number%20of%201%20Bits%20%E4%BD%8D1%E7%9A%84%E4%B8%AA%E6%95%B0.md) |
| 198 | [House Robber<br> 打家劫舍](https://leetcode-cn.com/problems/house-robber/) | [Java](java/src/198.%20HouseRobber.java) [Python3](py3/198.py) | Easy | `Dynamic Programming` | [:page_facing_up:](docs/198.%20House%20Robber%20%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8D.md) |
| 200 | [Number of Islands<br> 岛屿数量](https://leetcode-cn.com/problems/number-of-islands/) | [Java](java/src/200.%20NumberofIslands.java) | Medium | `Depth-first Search`, `Breadth-first Search`, `Union Find` | [:page_facing_up:](docs/200.%20Number%20of%20Islands%20%E5%B2%9B%E5%B1%BF%E6%95%B0%E9%87%8F.md) |
| 204 | [Count Primes<br> 计算质数](https://leetcode-cn.com/problems/count-primes/) | [Java](java/src/204.%20CountPrimes.java) | Easy | `Hash Table`, `Math` | [:page_facing_up:](docs/204.%20Count%20Primes%20%E8%AE%A1%E7%AE%97%E8%B4%A8%E6%95%B0.md) |
| 206 | [Reversed Linked List<br> 反转链表](https://leetcode-cn.com/problems/reverse-linked-list/) | [Java](java/src/206.%20ReversedLinkedList.java) [Python3](py3/206.py) | Easy | `Linked List` | [:page_facing_up:](docs/206.%20Reversed%20Linked%20List%20%E5%8F%8D%E8%BD%AC%E9%93%BE%E8%A1%A8.md) |
| 226 |  |  [Python3](py3/226.py) |  |  |  |
| 230 | [Kth Smallest Element in a BST<br> 二叉搜索树中第K小的元素](https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/) | [Java](java/src/230.%20KthSmallestElementinaBST.java) | Medium | `Tree`, `Binary Search` | [:page_facing_up:](docs/230.%20Kth%20Smallest%20Element%20in%20a%20BST%20%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%AC%ACK%E5%B0%8F%E7%9A%84%E5%85%83%E7%B4%A0.md) |
| 234 | [Palindrome Linked List<br> 回文链表](https://leetcode-cn.com/problems/palindrome-linked-list/) | [Java](java/src/234.%20PalidromeLinkedList.java) [Python3](py3/234.py) | Easy | `Linked List`, `Two Pointers` | [:page_facing_up:](docs/234.%20Palindrome%20Linked%20List%20%E5%9B%9E%E6%96%87%E9%93%BE%E8%A1%A8.md) |
| 237 | [Delete Node in a Linked List<br> 删除链表中的节点](https://leetcode-cn.com/problems/delete-node-in-a-linked-list/) | [Java](java/src/237.%20DeleteNodeInALinkedList.java) | Easy | `Linked List` | [:page_facing_up:](docs/237.%20Delete%20Node%20in%20a%20Linked%20List%20%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.md) |
| 238 |  |  [Python3](py3/238.py) |  |  |  |
| 242 | [Valid Anagram<br> 有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/) | [Java](java/src/242.%20ValidAnagram.java) | Easy | `Sort`, `Hash Table` | [:page_facing_up:](docs/242.%20Valid%20Anagram%20%E6%9C%89%E6%95%88%E7%9A%84%E5%AD%97%E6%AF%8D%E5%BC%82%E4%BD%8D%E8%AF%8D.md) |
| 268 | [Missing Number<br> 缺失数字](https://leetcode-cn.com/problems/missing-number/) | [Java](java/src/268.%20MissingNumber.java) | Easy | `Bit Manipulation`, `Array`, `Math` | [:page_facing_up:](docs/268.%20Missing%20Number%20%E7%BC%BA%E5%A4%B1%E6%95%B0%E5%AD%97.md) |
| 278 | [First Bad Version<br> 第一个错误的版本](https://leetcode-cn.com/problems/first-bad-version/) | [Java](java/src/278.%20FirstBadVersion.java) | Easy | `Binary Search` | [:page_facing_up:](docs/278.%20First%20Bad%20Version%20%E7%AC%AC%E4%B8%80%E4%B8%AA%E9%94%99%E8%AF%AF%E7%9A%84%E7%89%88%E6%9C%AC.md) |
| 283 |  |  [Python3](py3/283.py) |  |  |  |
| 326 | [Power of Three<br> 3的幂](https://leetcode-cn.com/problems/power-of-three/description/) | [Java](java/src/326.%20PowerofThree.java) | Easy | `Math` | [:page_facing_up:](docs/326.%20Power%20of%20Three%203%E7%9A%84%E5%B9%82.md) |
| 328 | [Odd Even Linked List<br> 奇偶链表](https://leetcode-cn.com/problems/odd-even-linked-list/) | [Java](java/src/328.%20OddEvenLinkedList.java) | Medium | `Linked List` | [:page_facing_up:](docs/328.%20Odd%20Even%20Linked%20List%20%E5%A5%87%E5%81%B6%E9%93%BE%E8%A1%A8.md) |
| 334 | [Increasing Triplet Subsequence<br> 递增的三元子序列](https://leetcode-cn.com/problems/increasing-triplet-subsequence/) | [Java](java/src/334.%20IncreasingTripletSubsequence.java) | Medium | `Two Pointers` | [:page_facing_up:](docs/334.%20Increasing%20Triplet%20Subsequence%20%E9%80%92%E5%A2%9E%E7%9A%84%E4%B8%89%E5%85%83%E5%AD%90%E5%BA%8F%E5%88%97.md) |
| 338 |  |  [Python3](py3/338.py) |  |  |  |
| 344 | [Reverse String<br> 反转字符串](https://leetcode-cn.com/problems/reverse-string/) | [Java](java/src/344.%20ReverseString.java) | Easy | `Two Pointers`, `String` | [:page_facing_up:](docs/344.%20Reverse%20String%20%E5%8F%8D%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2.md) |
| 347 | [Top K Frequent Elements<br> 前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements/) | [Java](java/src/347.%20TopKFrequentElements.java) [Python3](py3/347.py) | Medium | `Heap`, `Hash Table` | [:page_facing_up:](docs/347.%20Top%20K%20Frequent%20Elements%20%E5%89%8D%20K%20%E4%B8%AA%E9%AB%98%E9%A2%91%E5%85%83%E7%B4%A0.md) |
| 384 | [Shuffle an Array<br> 打乱数组](https://leetcode-cn.com/problems/shuffle-an-array/) | [Java](java/src/384.%20ShuffleanArray.java) | Medium | `Design` | [:page_facing_up:](docs/384.%20Shuffle%20an%20Array%20%E6%89%93%E4%B9%B1%E6%95%B0%E7%BB%84.md) |
| 387 | [First Unique Character in a String<br> 字符串中第一个唯一字符](https://leetcode-cn.com/problems/first-unique-character-in-a-string/) | [Java](java/src/387.%20FirstUniqueCharacterInAString.java) | Easy | `Hash Table`, `String` | [:page_facing_up:](docs/387.%20First%20Unique%20Character%20in%20a%20String%20%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%94%AF%E4%B8%80%E5%AD%97%E7%AC%A6.md) |
| 406 |  |  [Python3](py3/406.py) |  |  |  |
| 412 | [Fizz Buzz](https://leetcode-cn.com/problems/fizz-buzz/) | [Java](java/src/412.%20FizzBuzz.java) | Easy | `Math` | [:page_facing_up:](docs/412.%20Fizz%20Buzz.md) |
| 437 |  |  [Python3](py3/437.py) |  |  |  |
| 438 |  |  [Python3](py3/438.py) |  |  |  |
| 448 |  |  [Python3](py3/448.py) |  |  |  |
| 461 | [Hamming Distance<br> 汉明距离](https://leetcode-cn.com/problems/hamming-distance/) | [Java](java/src/461.%20HammingDistance.java) [Python3](py3/461.py) | Easy | `Bit Manipulation` | [:page_facing_up:](docs/461.%20Hamming%20Distance%20%E6%B1%89%E6%98%8E%E8%B7%9D%E7%A6%BB.md) |
| 538 |  |  [Python3](py3/538.py) |  |  |  |
| 543 |  |  [Python3](py3/543.py) |  |  |  |
| 572 |  |  [Python3](py3/572.py) |  |  |  |
| 581 |  |  [Python3](py3/581.py) |  |  |  |
| 617 |  |  [Python3](py3/617.py) |  |  |  |
| 647 |  |  [Python3](py3/647.py) |  |  |  |
| 697 | [Degree of an Array](https://leetcode.com/problems/degree-of-an-array/submissions/) |  [C++](cpp/src/697.cpp) | Easy | `Array` | [:page_facing_up:](docs/697.%20Degree%20of%20an%20Array.md) |
| 832 |  |  [C++](cpp/src/832.cpp) |  |  |  |
| 905 |  |  [C++](cpp/src/905.cpp) |  |  |  |
| 1114 | [Print in Order<br> 按序打印](https://leetcode-cn.com/problems/print-in-order/) | [Java](java/src/1114.%20PrintInOrder.java) | Easy | `Concurrency` | [:page_facing_up:](docs/1114.%20Print%20in%20Order%20%E6%8C%89%E5%BA%8F%E6%89%93%E5%8D%B0.md) |
| 1137 | [N-th Tribonacci Number<br> 第 N 个泰波那契数](https://leetcode-cn.com/problems/n-th-tribonacci-number/) | [Java](java/src/1137.%20NthTribonacciNumber.java) | Easy | `Recursion` | [:page_facing_up:](docs/1137.%20N-th%20Tribonacci%20Number%20%E7%AC%AC%20N%20%E4%B8%AA%E6%B3%B0%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0.md) |



## Statistics

- Total solved problems : 102
- Total docs : 77

Group by solution language:
- Total solutions via Java : 69
- Total solutions via Python3 : 50
- Total solutions via C++ : 18

Group by difficulty:
- Easy: 43
- Medium: 33
- Hard: 1

## License

This repository is licensed under the [MIT License](LICENSE).

``` 
MIT License

Copyright (c) 2018-2020 Zhenzhen Zhao

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```