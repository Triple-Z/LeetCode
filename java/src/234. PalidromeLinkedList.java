/*
 * @lc app=leetcode.cn id=234 lang=java
 *
 * [234] 回文链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        // copy elements into a list
        List<Integer> list = new ArrayList<>();
        for (ListNode i = head; i != null; i = i.next) {
            list.add(i.val);
        }

        int i = 0, j = list.size()-1;
        while (i < j) {
            if (!Objects.equals(list.get(i), list.get(j))) {
                return false;
            }

            i++; j--;
        }

        return true;

    }
}
// @lc code=end

