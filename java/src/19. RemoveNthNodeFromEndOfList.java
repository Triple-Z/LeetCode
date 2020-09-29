class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // dummy head
        ListNode dummy = new ListNode();
        dummy.next = head;

        ListNode prev = dummy, front = dummy;
        for (int i = 0; i < n+1; i++) front = front.next;
        while (front != null) {
            prev = prev.next;
            front = front.next;
        }

        // delete node
        prev.next = prev.next.next;
        
        return dummy.next;
    }
}