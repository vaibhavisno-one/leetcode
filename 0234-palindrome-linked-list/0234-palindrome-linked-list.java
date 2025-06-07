class Solution {
    private ListNode reverse(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode newHead = reverse(head.next);

        ListNode front = head.next;
        front.next = head;
        head.next = null;

        return newHead;
    }

    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) return true;

        // Step 1: Find the middle
        ListNode slow = head;
        ListNode fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // Step 2: Reverse the second half
        ListNode secondHalfStart = reverse(slow.next);
        ListNode reversedHead = secondHalfStart; // Save for restoration

        // Step 3: Compare both halves
        ListNode firstHalfStart = head;
        boolean isPalin = true;
        while (secondHalfStart != null) {
            if (firstHalfStart.val != secondHalfStart.val) {
                isPalin = false;
                break;
            }
            firstHalfStart = firstHalfStart.next;
            secondHalfStart = secondHalfStart.next;
        }

        // Step 4: Restore the list
        slow.next = reverse(reversedHead);

        return isPalin;
    }
}
