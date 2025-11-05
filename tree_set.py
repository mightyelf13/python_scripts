class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class TreeSet:
    def __init__(self):
        self.root = None

    def contains(self, x):
        return self._contains(self.root, x)

    def _contains(self, node, x):
        if node is None:
            return False
        if x == node.val:
            return True
        elif x < node.val:
            return self._contains(node.left, x)
        else:
            return self._contains(node.right, x)

    def add(self, x):
        self.root = self._add(self.root, x)

    def _add(self, node, x):
        if node is None:
            return Node(x)
        if x < node.val:
            node.left = self._add(node.left, x)
        elif x > node.val:
            node.right = self._add(node.right, x)
        return node

    def remove(self, x):
        self.root = self._remove(self.root, x)

    def _remove(self, node, x):
        if node is None:
            return None

        if x < node.val:
            node.left = self._remove(node.left, x)
        elif x > node.val:
            node.right = self._remove(node.right, x)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.val = self._get_min(node.right)
            node.right = self._remove(node.right, node.val)
        return node

    def _get_min(self, node):
        while node.left is not None:
            node = node.left
        return node.val

    def min(self):
        if self.root is None:
            return None
        return self._get_min(self.root)

    def max(self):
        if self.root is None:
            return None
        return self._get_max(self.root)

    def _get_max(self, node):
        while node.right is not None:
            node = node.right
        return node.val

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)

    def count(self, lo, hi):
        return self._count(self.root, lo, hi)

    def _count(self, node, lo, hi):
        if node is None:
            return 0

        if node.val < lo:
            return self._count(node.right, lo, hi)
        elif node.val > hi:
            return self._count(node.left, lo, hi)
        else:
            return 1 + self._count(node.left, lo, hi) + self._count(node.right, lo, hi)

    def replace(self, parent, n, p):
        if parent is None:
            self.root = p
        elif parent.left == n:
            parent.left = p
        elif parent.right == n:
            parent.right = p
        else:
            assert False, 'not a child'

def sample1():
    t = TreeSet()
    print(t.min())
    print(t.max())
    for x in [4, 2, 8, 6, 10]:
        t.add(x)
    t.add(4)
    print('size =', t.size())
    print('min =', t.min())
    print('max =', t.max())
    print('t.contains(8) =', t.contains(8))
    t.remove(8)
    print('t.contains(8) =', t.contains(8))
    print('size =', t.size())
    print('t.count(3, 7) =', t.count(3, 7))
if __name__ == "__main__":
 sample1()