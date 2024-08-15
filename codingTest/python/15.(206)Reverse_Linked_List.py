# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:

# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
 

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None  # 이전 노드를 가리킵니다 (초기값은 None)
        current = head  # 현재 노드를 가리킵니다 (초기값은 head)

        while current:
            next_node = current.next  # 현재 노드의 다음 노드를 임시 저장합니다.
            current.next = prev  # 현재 노드의 다음 노드를 이전 노드를 가리키도록 변경합니다.
            prev = current  # 이전 노드를 현재 노드로 업데이트합니다.
            current = next_node  # 현재 노드를 다음 노드로 이동합니다.

        return prev  # 새로운 head (뒤집어진 리스트의 첫 노드)를 반환합니다.

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
