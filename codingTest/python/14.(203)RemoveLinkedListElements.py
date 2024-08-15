# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Example 1:


# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# Example 2:

# Input: head = [], val = 1
# Output: []
# Example 3:

# Input: head = [7,7,7,7], val = 7
# Output: []
 

# Constraints:

# The number of nodes in the list is in the range [0, 104].
# 1 <= Node.val <= 50
# 0 <= val <= 50
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 가짜 헤드 노드를 만듭니다.
        dummy = ListNode(-1)
        dummy.next = head
        
        # 현재 노드를 가짜 헤드 노드로 설정합니다.
        current = dummy
        
        # 리스트를 순회하면서 값을 체크합니다.
        while current.next is not None:
            if current.next.val == val:
                # 다음 노드의 값이 val과 같다면, 그 노드를 건너뜁니다.
                current.next = current.next.next
            else:
                # 다음 노드의 값이 다르면, 현재 노드를 다음 노드로 이동합니다.
                current = current.next
        
        # 가짜 헤드 노드의 다음 노드를 반환합니다.
        return dummy.next

    # Helper function to create a linked list from a Python list
    def create_linked_list(lst):
        if not lst:
            return None
        head = ListNode(lst[0])
        current = head
        for value in lst[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    # Helper function to convert a linked list back to a Python list
    def linked_list_to_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result
