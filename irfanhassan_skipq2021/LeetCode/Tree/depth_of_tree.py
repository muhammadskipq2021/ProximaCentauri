class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))