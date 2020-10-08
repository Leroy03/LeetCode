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
            
#       Make a cycle here  
        curr.next = head
    
#       This is the original starting points
        curr = curr.next  
        # print(start, tail,curr.val,count)
        
#         Reduce the cycle times
        k %= count
    
#       New starting points
        for i in range(count-k):
            curr = curr.next
            # print(curr.val)
#       Answer print out the length of the original one which is has a cycle 
        for i in range(count):
            ans = ListNode(curr.val, ans)
            curr = curr.next
            
#             Reverse Here
        pre = None 
        curr = ans
        while curr:
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp 
        ans = pre
        
        return ans
