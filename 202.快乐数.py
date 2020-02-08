class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = n    #利用快慢指针，快走2步，慢走1步。二者相等即为一个循环周期。
        fast = n
        slow = sum([ int(i)*int(i) for i in str(slow)])
        fast = sum([ int(i)*int(i) for i in str(fast)])
        fast = sum([ int(i)*int(i) for i in str(fast)])
        while slow!=fast:
            print slow, fast
            slow = sum([ int(i)*int(i) for i in str(slow)])
            fast = sum([ int(i)*int(i) for i in str(fast)])
            fast = sum([ int(i)*int(i) for i in str(fast)])
            
        return slow==1
