/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null) return null;
        
        ListNode back = head;
        ListNode current = head.next;
        while (current != null) {
            ListNode forward = current.next;
            // reverse
            current.next = back;
            if (back == head) back.next = null;
            back = current;
            current = forward;
        }
        return back; // new head
    }
}