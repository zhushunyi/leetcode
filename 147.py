# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        #print(head.next)
        #print(head.next.next.val)
        '''temp = head.next
        new_linked_list = head
        new_linked_list.next = None
        new_head = new_linked_list
        print(new_linked_list.val)
        while temp != None:
            if new_head.next != None:
                if temp.val > new_head.val:
                    temp.next = new_head.next
                    new_head.next = temp
                    new_head = new_head.next
                else:
                    temp.next = new_head
                    new_head = new_linked_list'''
        new_list = ListNode(float("-inf"))
        begin = new_list
        end = new_list
        flag = head
        while flag != None:
            if end.val < flag.val:
                end.next = flag
                end = flag
                flag = flag.next
            else:
                temp = flag.next
                end.next = temp
                while begin.next != None and begin.next.val < flag.val:
                    begin = begin.next
                flag.next = begin.next
                begin.next = flag
                begin = new_list
                flag = temp
        return new_list.next