# 参考官方解答，利用回溯算法。回溯函数backtrack(),以当前的组合结果
#和接下来的输入数字作为参数。
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
                 
        def backtrack(result, next_digits):
            if len(next_digits)==0:
                output.append(result)
            else:
                for s in phone[next_digits[0]]:
                    backtrack(result + s, next_digits[1:])
        output = []
        if digits:
            backtrack("", digits)
        return output
            
