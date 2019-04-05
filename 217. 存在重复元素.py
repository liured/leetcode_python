class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==0:
            return False
        nums.sort()      #先排序
        for i in range(len(nums)-1):     #再相邻判断
            if nums[i]==nums[i+1]:
                return True
        return False
        
