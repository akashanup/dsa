"""
# Intuition

Since both linked lists are already sorted, we can merge them in a similar way to the merge step of Merge Sort.

We maintain a pointer to the end of the merged list and compare the current nodes of both lists. The smaller node is appended to the merged list, and its pointer is advanced. Once one list is exhausted, we can directly attach the remaining nodes from the other list since they are already sorted.

A sentinel (dummy) node is used to simplify edge cases such as handling the head of the merged list.

# Approach

1. Create a sentinel node and use a `curr` pointer to build the merged list.
2. Traverse both lists while neither is empty:
   - Compare the current values of `list1` and `list2`.
   - Attach the smaller node to `curr.next`.
   - Move the corresponding list pointer forward.
   - Advance `curr`.
3. After the loop, at most one list still contains nodes.
4. Attach the remaining list directly to `curr.next`.
5. Return `sentinel.next`, which points to the head of the merged list.

# Complexity

- Time complexity:
  
  $$O(m+n)$$
  
  where `m` and `n` are the lengths of `list1` and `list2`. Each node is visited exactly once.

<br>

- Space complexity:
  
  $$O(1)$$
  
  Only a few pointers are used, and the existing nodes are reused without creating additional data structures.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        sentinel = ListNode()
        curr = sentinel

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        if list1:
            curr.next = list1

        if list2:
            curr.next = list2

        return sentinel.next