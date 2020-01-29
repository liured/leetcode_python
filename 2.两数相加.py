# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        res = None
        flag = 0
        p = None
        q = None
        p = l1
        q = l2
        while p!=None or q!=None:
            p_val = p.val if p!=None else 0
            q_val = q.val if q!=None else 0
            sum = p_val + q_val
            sum_1 = (sum+1) if flag else sum
            x = sum_1%10
            if res==None:
                head = ListNode(x)
                res = head
            else:
                res.next = ListNode(x)
                res = res.next
            flag = sum_1/10
                
            if p:
                p = p.next
            if q:
                q = q.next
            
        if flag:
            res.next = ListNode(1)
            res = res.next
                
        return head
        
l1 = ListNode(1)
#l1.next = ListNode(4)
#l1.next.next = ListNode(3)
#while l1:
#    print l1.val
#    l1 = l1.next
l2 = ListNode(9)
l2.next = ListNode(9)
#l2.next.next = ListNode(4)
#while l2:
#    print l2.val
#    l2 = l2.next
S = Solution()
l = S.addTwoNumbers(l1,l2)           
while l:
    print l.val
    l = l.next
