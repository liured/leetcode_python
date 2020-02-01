#记录前面不重复的元素个数res，，记录当前元素cur，比较数组后面的元素与当前元素是否相同，不相同则res+1，并赋值改位置，修改cur。
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        if len(nums)==0:
            return 0
        cur = nums[0]
        for it in nums[1:]:
            if it==cur:
                continue
            else:
                res = res+1
                nums[res] = it
                cur = it
       # print nums
        return res+1
        
#标准解法，用双指针法。改方法会改变数组原本的元素。
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for j in range(1,len(nums)):
            if nums[j]!=nums[i]:
                nums[i+1]=nums[j]
                i += 1
#        print nums
        return i+1
