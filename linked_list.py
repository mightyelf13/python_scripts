class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, values):
        self.head = None
        for value in reversed(values):
            self.head = Node(value, next=self.head)

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def len(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def get(self, n):
        current = self.head
        for _ in range(n):
            current = current.next
        return current.value

    def has(self, x):
        current = self.head
        while current:
            if current.value == x:
                return True
            current = current.next
        return False

    def delete(self, x):
        current = self.head

        if current and current.value == x:
            self.head = current.next
            return

        prev = None
        while current and current.value != x:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next

    def rotate(self):
        if self.head and self.head.next:
            current = self.head
            while current.next.next:
                current = current.next
            current.next.next = self.head
            self.head = current.next
            current.next = None

    def starts_with(self, m):
        p, q = self.head, m.head
        while q:
            if not p or p.value != q.value:
                return False
            p, q = p.next, q.next
        return True

    def contains(self, m):
        p, q = self.head, m.head
        while p:
            if self.starts_with(m):
                return True
            p = p.next
        return False

    def ends_with(self, m):
        len_self, len_m = self.len(), m.len()
        if len_self < len_m:
            return False

        p, q = self.head, m.head
        for _ in range(len_self - len_m):
            p = p.next

        while p and q:
            if p.value != q.value:
                return False
            p, q = p.next, q.next
        return True

if __name__ == "__main__":
    l = LinkedList([2, 7, 4, 9, 18, 19, 22])
    print(l.to_list())
    print(l.len())
    print(l.get(3))
    print(l.has(17))

    o = LinkedList([7])
    print(o.to_list())
    print(o.len())

    e = LinkedList([])
    print(e.to_list())
    print(e.len())