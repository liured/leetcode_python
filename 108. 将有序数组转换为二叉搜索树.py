'''
取数组的中间元素作为根节点，将数组分为左右两个部分，递归建立左右子树。
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==0:
            return None
        min_idx = len(nums) // 2
        node = TreeNode(nums[min_idx])
        node.left = self.sortedArrayToBST(nums[:min_idx])
        node.right = self.sortedArrayToBST(nums[min_idx+1:])
        return node
