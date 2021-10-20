<!-- omit in toc -->
# Depth-first Search

- [Problems](#problems)
- [Statistics](#statistics)

## Problems

| # | Title | Solution | Difficulty | Topics | Doc |
|:----:|:----:|:----:|:----:|:----:|:----:|
| [<span id="problem-98">98</span>](#problem-98 "#98") | [Valid Binary Search Tree <br>验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree/ "https://leetcode-cn.com/problems/validate-binary-search-tree/") | [Java](../../java/src/98.%20ValidBinarySearchTree.java "java/src/98.%20ValidBinarySearchTree.java") [Go](../../go/src/98.go "go/src/98.go") [Python3](../../py3/98.py "py3/98.py") | Medium | `Tree`, `Depth-first Search` | [:page_facing_up:](../../docs/98.%20Valid%20Binary%20Search%20Tree%20%E9%AA%8C%E8%AF%81%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.md "docs/98.%20Valid%20Binary%20Search%20Tree%20%E9%AA%8C%E8%AF%81%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.md") |
| [<span id="problem-101">101</span>](#problem-101 "#101") | [Symmetric Tree <br>对称二叉树](https://leetcode-cn.com/problems/symmetric-tree/ "https://leetcode-cn.com/problems/symmetric-tree/") | [Java](../../java/src/101.%20SymmetricTree.java "java/src/101.%20SymmetricTree.java") [Python3](../../py3/101.py "py3/101.py") | Easy | `Tree`, `Depth-first Search`, `Breadth-first Search` | [:page_facing_up:](../../docs/101.%20Symmetric%20Tree%20%E5%AF%B9%E7%A7%B0%E4%BA%8C%E5%8F%89%E6%A0%91.md "docs/101.%20Symmetric%20Tree%20%E5%AF%B9%E7%A7%B0%E4%BA%8C%E5%8F%89%E6%A0%91.md") |
| [<span id="problem-104">104</span>](#problem-104 "#104") | [Maximum Depth of Binary Tree <br>二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/ "https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/") | [Java](../../java/src/104.%20MaximumDepthOfBinaryTree.java "java/src/104.%20MaximumDepthOfBinaryTree.java") [Go](../../go/src/104.go "go/src/104.go") [Python3](../../py3/104.py "py3/104.py") | Easy | `Tree`, `Depth-first Search` | [:page_facing_up:](../../docs/104.%20Maximum%20Depth%20of%20Binary%20Tree%20%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%A4%A7%E6%B7%B1%E5%BA%A6.md "docs/104.%20Maximum%20Depth%20of%20Binary%20Tree%20%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%A4%A7%E6%B7%B1%E5%BA%A6.md") |
| [<span id="problem-105">105</span>](#problem-105 "#105") | [Construct Binary Tree from Preorder and Inorder Traversal <br>从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/ "https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/") | [Java](../../java/src/105.%20ConstructBinaryTreefromPreorderandInorderTraversal.java "java/src/105.%20ConstructBinaryTreefromPreorderandInorderTraversal.java") | Medium | `Array`, `Tree`, `Depth-first Search` | [:page_facing_up:](../../docs/105.%20Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal%20%E4%BB%8E%E5%89%8D%E5%BA%8F%E4%B8%8E%E4%B8%AD%E5%BA%8F%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97%E6%9E%84%E9%80%A0%E4%BA%8C%E5%8F%89%E6%A0%91.md "docs/105.%20Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal%20%E4%BB%8E%E5%89%8D%E5%BA%8F%E4%B8%8E%E4%B8%AD%E5%BA%8F%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97%E6%9E%84%E9%80%A0%E4%BA%8C%E5%8F%89%E6%A0%91.md") |
| [<span id="problem-108">108</span>](#problem-108 "#108") | [Convert Sorted Array to Binary Search Tree <br>将有序数组转换为二叉树](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/ "https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/") | [Java](../../java/src/108.%20ConvertSortedArrayToBinarySearchTree.java "java/src/108.%20ConvertSortedArrayToBinarySearchTree.java") [Go](../../go/src/108.go "go/src/108.go") | Easy | `Tree`, `Depth-first Search` | [:page_facing_up:](../../docs/108.%20Convert%20Sorted%20Array%20to%20Binary%20Search%20Tree%20%E5%B0%86%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E8%BD%AC%E6%8D%A2%E4%B8%BA%E4%BA%8C%E5%8F%89%E6%A0%91.md "docs/108.%20Convert%20Sorted%20Array%20to%20Binary%20Search%20Tree%20%E5%B0%86%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E8%BD%AC%E6%8D%A2%E4%B8%BA%E4%BA%8C%E5%8F%89%E6%A0%91.md") |
| [<span id="problem-114">114</span>](#problem-114 "#114") | [Flatten Binary Tree to Linked List <br>二叉树展开为链表](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/ "https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/") | [Java](../../java/src/114.%20FlattenBinaryTreetoLinkedList.java "java/src/114.%20FlattenBinaryTreetoLinkedList.java") | Medium | `Tree`, `Depth-first Search` | [:page_facing_up:](../../docs/114.%20Flatten%20Binary%20Tree%20to%20Linked%20List%20%E4%BA%8C%E5%8F%89%E6%A0%91%E5%B1%95%E5%BC%80%E4%B8%BA%E9%93%BE%E8%A1%A8.md "docs/114.%20Flatten%20Binary%20Tree%20to%20Linked%20List%20%E4%BA%8C%E5%8F%89%E6%A0%91%E5%B1%95%E5%BC%80%E4%B8%BA%E9%93%BE%E8%A1%A8.md") |
| [<span id="problem-116">116</span>](#problem-116 "#116") | [Populating Next Right Pointers in Each Node <br>填充每个节点的下一个右侧节点指针](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/ "https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/") | [Java](../../java/src/116.%20PopulatingNextRightPointersinEachNode.java "java/src/116.%20PopulatingNextRightPointersinEachNode.java") | Medium | `Tree`, `Depth-first Search` | [:page_facing_up:](../../docs/116.%20Populating%20Next%20Right%20Pointers%20in%20Each%20Node%20%E5%A1%AB%E5%85%85%E6%AF%8F%E4%B8%AA%E8%8A%82%E7%82%B9%E7%9A%84%E4%B8%8B%E4%B8%80%E4%B8%AA%E5%8F%B3%E4%BE%A7%E8%8A%82%E7%82%B9%E6%8C%87%E9%92%88.md "docs/116.%20Populating%20Next%20Right%20Pointers%20in%20Each%20Node%20%E5%A1%AB%E5%85%85%E6%AF%8F%E4%B8%AA%E8%8A%82%E7%82%B9%E7%9A%84%E4%B8%8B%E4%B8%80%E4%B8%AA%E5%8F%B3%E4%BE%A7%E8%8A%82%E7%82%B9%E6%8C%87%E9%92%88.md") |
| [<span id="problem-200">200</span>](#problem-200 "#200") | [Number of Islands <br>岛屿数量](https://leetcode-cn.com/problems/number-of-islands/ "https://leetcode-cn.com/problems/number-of-islands/") | [Java](../../java/src/200.%20NumberofIslands.java "java/src/200.%20NumberofIslands.java") | Medium | `Depth-first Search`, `Breadth-first Search`, `Union Find` | [:page_facing_up:](../../docs/200.%20Number%20of%20Islands%20%E5%B2%9B%E5%B1%BF%E6%95%B0%E9%87%8F.md "docs/200.%20Number%20of%20Islands%20%E5%B2%9B%E5%B1%BF%E6%95%B0%E9%87%8F.md") |


## Statistics

- Total solved problems : 8
- Total docs : 8

Group by solution language:
- Total solutions via Java : 8
- Total solutions via Go : 3
- Total solutions via Python3 : 3
- Total solutions via C++ : 0

Group by difficulty:
- Easy: 3
- Medium: 5
- Hard: 0