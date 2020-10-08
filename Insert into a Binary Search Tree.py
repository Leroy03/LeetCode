"""
My idea is doing a binary Tree - go to left if it is smaller than the node and so on.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        head = root
#       If it is a new Node  
        if root == None:
            root = TreeNode(val)
            return root
#       
        while True:
            # print("1")
            # print(root.right)
#         If left and right have node -> it must continue go down 
            if root.left != None and root.right != None:
                if root.val > val:
                    root = root.left
                    continue
                    # print("2")
                else:
                    root = root.right
                    continue
                    # print("3")
#           If left has no Node and smaller than the Node -> it must be that place (Leaf)          
            if root.left == None and root.val > val:
                # print(root)
                root.left = TreeNode(val)
                # print(root)
                # print("4")
                break
#           If right has no Node and bigger than the Node -> it must be that place (Leaf)          
            if root.right == None and root.val < val:
                root.right = TreeNode(val)
                # print("5")
                break
#           The only way to go down
            if root.left == None:
                root = root.right
                continue
            else:
                root = root.left
                continue
        return head
