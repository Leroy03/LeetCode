"""
My idea is make it as a cycle and change the starting points 'K' times and then print out the whole node
"""
class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if k == 0:
            return head
        curr = head
        start = curr.val
        ans = None
        count = 1
        
        while curr.next:
            count += 1
            curr = curr.next 
        tail = curr.val
        curr.next = head
        curr = curr.next  # Begin
        # print(start, tail,curr.val,count)
        k %= count
        for i in range(count-k):
            curr = curr.next
            # print(curr.val)
    
        for i in range(count):
            ans = ListNode(curr.val, ans)
            curr = curr.next
        pre = None 
        curr = ans
        while curr:
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp 
        ans = pre
        return ans
