class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode();
        ListNode p3 = dummy;
        ListNode p1 = l1, p2 = l2;
        int ci = 0;

        while (p1 != null || p2 != null) {
            int n1 = p1 != null ? p1.val : 0;
            int n2 = p2 != null ? p2.val : 0;
            int sum = n1 + n2 + ci;
            int curVal = sum % 10;
            ci = sum / 10;

            ListNode node = new ListNode(curVal);
            p3.next = node;
            p3 = node;

            p1 = p1 != null ? p1.next : null;
            p2 = p2 != null ? p2.next : null;            
        }

        if (ci > 0) {
            p3.next = new ListNode(ci);
        }
        
        return dummy.next;
    }
}