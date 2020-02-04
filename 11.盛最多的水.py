#利用双指针法，比较左右指针，数值小的加1.
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0  
        right = len(height)-1
        maxArea = 0  
        while left < right:
            if height[left] < height[right]:
                maxArea = max(maxArea, (right-left)*height[left])
                left += 1
            else:
                maxArea = max(maxArea, (right-left)*height[right])
                right -= 1
        return maxArea
