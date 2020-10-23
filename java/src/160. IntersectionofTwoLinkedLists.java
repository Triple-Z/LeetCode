public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) return null;

        ListNode pA = headA, pB = headB;
        boolean twice = false;
        while (pA != pB) {
            if (pA.next == null && twice) return null;
            if (pA.next == null && !twice) twice = true;
            pA = pA.next == null ? headB : pA.next;
            pB = pB.next == null ? headA : pB.next;
        }

        return pA;
    }
}