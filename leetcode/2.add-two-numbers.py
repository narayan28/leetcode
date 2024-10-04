#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        # Initialize a dummy node to form the result list
        dummy = ListNode(0)
        current = dummy
        carry = 0

        # Traverse both lists
        while l1 or l2:
            # Get values from the nodes, if present
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum of the values and the carry
            total = val1 + val2 + carry
            carry = total // 10  # Update the carry for the next iteration
            total = total % 10   # The digit to store in the current node

            # Create a new node with the sum and attach it to the result list
            current.next = ListNode(total)
            current = current.next

            # Move to the next nodes in l1 and l2, if they exist
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        # If there's a carry left at the end, create a new node for it
        if carry > 0:
            current.next = ListNode(carry)

        # Return the result list, skipping the dummy node
        return dummy.next

# @lc code=end

