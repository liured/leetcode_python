#方法1，用HashMap映射字符和值，如果当前字符代表的值不小于其右边，则加上该值，否则减去该值。
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        R = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(len(s)):
            if i<len(s)-1 and R[s[i]]<R[s[i+1]]:
                res -= R[s[i]]
            else:
                res += R[s[i]]
                
        return res
                
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        p = 0
        summ = 0
        if len(s)==0:
            return summ
        while p<len(s):
            if s[p]=='I':
                if (p+1)<len(s) and s[p+1]=='V':
                    summ += 4
                    p += 1
                elif (p+1)<len(s) and s[p+1]=='X':
                    summ += 9
                    p += 1
                else:
                    summ += 1
            elif s[p]=='X':
                if (p+1)<len(s) and s[p+1]=='L':
                    summ += 40
                    p += 1
                elif (p+1)<len(s) and s[p+1]=='C':
                    summ += 90
                    p += 1
                else:
                    summ += 10
            elif s[p]=='C':
                if (p+1)<len(s) and s[p+1]=='D':
                    summ += 400
                    p += 1
                elif (p+1)<len(s) and s[p+1]=='M':
                    summ += 900
                    p += 1
                else:
                    summ += 100
                
            elif s[p]=='V':
                summ += 5
            elif s[p]=='L':
                summ += 50
            elif s[p]=='D':
                summ += 500
            else:
                summ += 1000
            p += 1
        return summ                
        
        
        
        
string = "MCMXCIV"           
S = Solution()
print S.romanToInt(string)
          
