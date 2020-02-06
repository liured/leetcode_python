class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)
        res = []
        if not nums or length<3:
            return []
        for i in range(length):
            if nums[i]>0:    # 大于0直接返回
                return res
            if nums[i]==nums[i-1] and i>0:  #当前值与前面位置i的值重复，继续循环
                continue
            left = i+1
            right = length-1
            while left<right:    # 左指针小于右指针
                if nums[i]+nums[left]+nums[right]==0:
                    res.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:  # 排除左边可能重复
                        left += 1
                    while left<right and nums[right]==nums[right-1]:   # 排除右边可能重复
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif nums[i]+nums[left]+nums[right]>0:  
                    right -= 1
                else:
                    left += 1
        return res
        
