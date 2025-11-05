class Node:
    def __init__(self, v, l=None, r=None):
        self.value = v
        self.left = l
        self.right = r
def triple(root):
    if root is None:
        return None
    def go(node):
        if node is None:
            return None
        if node.left and node.right and node.value == node.left.value == node.right.value:
            return node.value
        left_triple = go(node.left)
        right_triple = go(node.right)
        if left_triple:
            return left_triple
        if right_triple:
            return right_triple
    return go(root)