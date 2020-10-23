class Solution {
    public ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null) return head;

        ListNode odds = new ListNode();
        ListNode ans = odds;
        ListNode evens = new ListNode();
        ListNode evensHead = evens;
        int counter = 1;
        
        while (head != null) {
            if (counter % 2 == 0) {
                // even
                evens.next = head;
                evens = evens.next;
            } else {
                // odd
                odds.next = head;
                odds = odds.next;
            }

            counter++;
            head = head.next;
        }

        odds.next = evensHead.next;
        evens.next = null;

        return ans.next;

    }
}