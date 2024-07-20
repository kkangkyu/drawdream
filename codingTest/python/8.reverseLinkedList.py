class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        list = head
        list.reverse()

        return list


print(Solution().reverseList([1, 2, 3, 4, 5]))
