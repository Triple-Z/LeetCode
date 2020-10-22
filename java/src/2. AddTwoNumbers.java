class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if (l1 == null) return l2;
        if (l2 == null) return l1;

        int ci = 0;
        int curVal = 0;
        ListNode p1 = l1;
        ListNode p2 = l2;
        ListNode ans = new ListNode();
        ListNode last = ans;
        while (p1 != null && p2 != null) {
            int tmp = p1.val + p2.val + ci;
            curVal = tmp % 10;
            ci = tmp / 10;

            // create a new node
            ListNode node = new ListNode(curVal);
            last.next = node;
            last = node;
            
            p1 = p1.next;
            p2 = p2.next;
        }

        while (p1 != null) {
            int tmp = p1.val + ci;
            curVal = tmp % 10;
            ci = tmp / 10;

            // create a new node
            ListNode node = new ListNode(curVal);
            last.next = node;
            last = node;
            
            p1 = p1.next;
        }

        while (p2 != null) {
            int tmp = p2.val + ci;
            curVal = tmp % 10;
            ci = tmp / 10;

            // create a new node
            ListNode node = new ListNode(curVal);
            last.next = node;
            last = node;

            p2 = p2.next;
        }

        if (ci != 0) {
            // create a new node
            ListNode node = new ListNode(ci);
            last.next = node;
            last = node;
        }

        return ans.next;
    }
}