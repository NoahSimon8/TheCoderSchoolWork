

class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

    def insert(self, d):
        if d <= self.data:
            if self.left is None:
                self.left = Node(d)
            else:
                self.left.insert(d)
        else:
            if self.right is None:
                self.right = Node(d)
            else:
                self.right.insert(d)

    def search(self, d):
        if d == self.data:
            return True
        if d < self.data:
            if self.left is None:
                return False
            else:
                return self.left.search(d)
        else:
            if self.right is None:
                return False
            else:
                return self.right.search(d)

    def preorder(self):
        print(self.data)
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.data)
        if self.right is not None:
            self.right.inorder()

    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print(self.data)

    def delete(self, d):
        if d == self.data:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                left_tree = self.left
                right_tree = self.right
                cur = right_tree
                if cur.left is not None:
                    while cur.left is not None:
                        parent = cur
                        cur = cur.left
                    parent.left = cur.delete(cur.data)
                    cur.right = right_tree
                cur.left = left_tree
                return cur
        if d < self.data:
            if self.left is None:
                return self
            self.left = self.left.delete(d)
        else:
            if self.right is None:
                return self
            self.right = self.right.delete(d)
        return self

    def __display(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left.__display()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right.__display()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left.__display()
        right, m, q, y = self.right.__display()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
    def __str__(self):
        tree = self.__display()[0]
        string = ""
        for branch in tree:
            string += branch + "\n"
        return string


# bst = Node(10)
# bst.insert(5)
# bst.insert(15)
# bst.preorder()
# bst.inorder()
# bst.postorder()
# bst = bst.delete(5)
# print(bst.search(5))
# print(bst)



nums = [20, 5, 3, 2, 1, 4, 6, 7, 20, 11, 35,
        25, 21, 45, 40, 36, 38, 50, 48, 60]
bst = Node(nums[0])
for i in range(1, len(nums)):
    bst.insert(nums[i])

print(bst)
bst = bst.delete(11)
bst = bst.delete(2)
bst = bst.delete(35)
bst = bst.delete(5)
bst = bst.delete(20)
print(bst)

"""Error Appears"""
# bst = Node(10)
# print(bst)
# bst = bst.delete(bst, 10)
# print(bst)
# bst = bst.delete(bst, 10)
# print(bst)
# bst.insert(20)
# bst.insert(25)
# print(bst)