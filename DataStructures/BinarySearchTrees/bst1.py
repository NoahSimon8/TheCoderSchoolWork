

class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, d):
        self.root = Node(d)

    def insert(self, node, d):
        if d <= node.data:
            if node.left is None:
                node.left = Node(d)
            else:
                self.insert(node.left, d)
        else:
            if node.right is None:
                node.right = Node(d)
            else:
                self.insert(node.right, d)

    def search(self, node, d):
        if d == node.data:
            return True
        if d < node.data:
            if node.left is None:
                return False
            else:
                return self.search(node.left, d)
        else:
            if node.right is None:
                return False
            else:
                return self.search(node.right, d)

    def preorder(self, node):
        if node is not None:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)

    def delete(self, node, d):
        if node is None:
            return node
        if d == node.data:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                left_tree = node.left
                right_tree = node.right
                cur = right_tree
                if cur.left is not None:
                    while cur.left is not None:
                        parent = cur
                        cur = cur.left
                    parent.left = self.delete(cur, cur.data)
                    cur.right = right_tree
                cur.left = left_tree
                return cur
        if d < node.data:
            node.left = self.delete(node.left, d)
        else:
            node.right = self.delete(node.right, d)
        return node

    def __display(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.right is None and node.left is None:
            line = '%s' % node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self.__display(node.left)
            s = '%s' % node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self.__display(node.right)
            s = '%s' % node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.__display(node.left)
        right, m, q, y = self.__display(node.right)
        s = '%s' % node.data
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
        string = ""
        if self.root is not None:
            tree = self.__display(self.root)[0]
            for branch in tree:
                string += branch + "\n"
        return string


bst = BinarySearchTree(10)
bst.insert(bst.root, 5)
bst.insert(bst.root, 15)
bst.preorder(bst.root)
bst.inorder(bst.root)
bst.postorder(bst.root)
bst.root = bst.delete(bst.root, 5)
print(bst.search(bst.root, 5))
print(bst)

# nums = [20, 5, 3, 2, 1, 4, 6, 7, 20, 11, 35,
#         25, 21, 45, 40, 36, 38, 50, 48, 60]
# bst = BinarySearchTree(nums[0])
# for i in range(1, len(nums)):
#     bst.insert(bst.root, nums[i])
# print(bst)
# bst.root = bst.delete(bst.root, 11)
# bst.root = bst.delete(bst.root, 2)
# bst.root = bst.delete(bst.root, 35)
# bst.root = bst.delete(bst.root, 5)
# bst.root = bst.delete(bst.root, 20)
# print(bst)

"""Error Appears"""
# bst = BinarySearchTree(10)
# print(bst)
# bst.root = bst.delete(bst.root, 10)
# print(bst)
# bst.root = bst.delete(bst.root, 10)
# print(bst)
# bst.insert(bst.root, 20)
# bst.insert(bst.root, 25)
# print(bst)