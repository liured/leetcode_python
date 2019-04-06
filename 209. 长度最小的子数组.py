'''
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
'''
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        b = 0        #利用双指针，这是左指针
        e = 0        #右指针
        m = 0        #连续和
        min_len = len(nums) + 1
        while b<len(nums):         #结束条件是开始指针小于遍历长度
            if e<len(nums) and m<s:       #和小于s，移动右指针
                m += nums[e]
                e += 1
            else:                        #否则，移动左指针
                m -= nums[b]
                b += 1
            if m>=s:
                min_len = min(min_len, e - b)
        if min_len == len(nums) + 1:
            return 0
        return min_len
        
