class Solution(object):
	def removeNthFromEnd(self, head, n):
		"""
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""
		if not head or n<=0:
			return head
		p = ListNode(-1)
		p.next,a,b,k = head,p,p,0
		while a.next:
			a,k = a.next,k+1
		if k<n:
			return head
		num = k-n
		while num>0:
			b,num = b.next,num-1
		b.next = b.next.next
		return p.next