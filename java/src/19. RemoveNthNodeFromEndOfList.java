class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // get length
        ListNode node = head;
        int len = 0;
        while (node != null) {
            len++;
            node = node.next;
        }

        // get node
        node = head;
        for (int i = 1; i < len - n; i++) {
            node = node.next;
        }
        if (len == n) {
            // delete head
            head = node.next;
        } else {
            ListNode deNode = node.next;
            // delete deNode
            node.next = deNode.next;
        }
        
        return head;
    }
}
