# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
# Constraints:
# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.
 
# Follow up: Can you solve it using O(1) (i.e. constant) memory?
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 두 개의 포인터를 사용합니다. 하나는 slow, 다른 하나는 fast.
        slow = head
        fast = head

        # fast와 fast.next가 None이 아닌 동안 루프를 돈다.
        while fast and fast.next:
            slow = slow.next         # slow는 한 번에 한 노드씩 이동
            fast = fast.next.next    # fast는 한 번에 두 노드씩 이동

            # 만약 slow와 fast가 만나면, 사이클이 존재함을 의미합니다.
            if slow == fast:
                return True

        # fast가 끝에 도달하면 사이클이 없다는 뜻입니다.
        return False

    # Helper function to create a linked list with a cycle
    def create_cyclic_list(values, pos):
        if not values:
            return None
        
        head = ListNode(values[0])
        current = head
        cycle_node = None
        
        for i in range(1, len(values)):
            current.next = ListNode(values[i])
            current = current.next
        if i == pos:
            cycle_node = current
    
        if pos != -1:
            current.next = cycle_node
        
        return head
