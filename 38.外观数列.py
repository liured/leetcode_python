'''
【参考答案】
创建一个栈
遍历字符串：
1.当字符与栈内字符相同或者栈为空时入栈
2.当字符与栈内字符不相同时，取栈的长度+栈内字符，清空栈并将新的元素入栈
（注意：最后栈不为空所以在循环结束后需要在进行一次取栈的长度+栈内字符的操作）

'''
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        nums = []
        nums.append("")
        nums.append("1")
        if n==1:
            return nums[1]
        else:
            for i in range(2, n+1):
                z = []
                string = ""
                for s in nums[i-1]:
                    if z==[] or s==z[0]:
                        z.append(s)
                    else:
                        string += str(len(z))
                        string += z[0]
                        z = []
                        z.append(s)
                string += str(len(z))
                string += z[0]
                nums.append(string)
        return nums[n]
