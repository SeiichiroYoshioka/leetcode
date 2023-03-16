#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        a = self.linkedlist2list(l1)
        b = self.linkedlist2list(l2)
        res = 0
        order = 0
        while True:
            if len(a) == 0 and len(b) == 0:
                break
            if len(a) != 0:
                a_s = a.pop(0)
            else:
                a_s = 0
            if len(b) != 0:
                b_s = b.pop(0)
            else:
                b_s = 0
            res += (a_s + b_s) * 10**order
            order += 1
        result = ListNode()

        r = result
        for i, s in enumerate(str(res)[::-1]):
            result.val = int(s)
            if i == len(str(res)) - 1:
                break
            result.next = ListNode()
            result = result.next
        return r

    def linkedlist2list(self, li):
        res = []
        while True:
            res.append(li.val)
            if li.next is None:
                break
            else:
                li = li.next
        return res


# @lc code=end
