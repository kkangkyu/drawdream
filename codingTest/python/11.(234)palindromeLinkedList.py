# Given the head of a singly linked list, return true if it is a 
# palindrome
#  or false otherwise.

# Example 1:
# Input: head = [1,2,2,1]
# Output: true
# Example 2:
# Input: head = [1,2]
# Output: false
# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
# Follow up: Could you do it in O(n) time and O(1) space?


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #다음 노드에 들어갔을때는 회귀적으로 계속해서 비교해야함
        if head.next == None:
            return True
        
        #두개의 포인터를 사용해서 중간을 찾아야함
        slow = head
        fast = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        #slow를 중간으로 두고 slow부터 뒤로 가면서 역순으로 만들어줌
        prev = None
        cur = slow.next
        while cur != None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        #역순으로 만든 노드와 head를 비교
        while prev != None:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True