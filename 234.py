# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        new_list = []
        temp = head
        while temp is not None:
            new_list.append(temp.val)
            temp = temp.next
        return new_list == new_list[::-1]