# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None

        parent = None
        node = root

        while node is not None and node.val != key:
            parent = node
            if key > node.val:
                node = node.right
            else:
                node = node.left

        if node is None:
            return root

        if node.left is None and node.right is None:
            if parent is None: return None
            if parent.left == node: parent.left = None
            else: parent.right = None

        elif node.right is None:
            if parent is None: return node.left
            if parent.left == node: parent.left = node.left
            else: parent.right = node.left

        elif node.left is None:
            if parent is None: return node.right
            if parent.left == node: parent.left = node.right
            else: parent.right = node.right

        else:
            successor_parent = node
            successor = node.right
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left
            node.val = successor.val
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

        return root
