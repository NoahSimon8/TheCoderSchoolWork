"""
self balencing Idea:
have a self.root varable, then just switch when necassary

"""

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

    def breadthfirstsearch(self,layer=0,list=[]):
        if len(list)<layer+1:
            list.append([])
        list[layer].append(self.data)
        if self.left!=None:
            list=self.left.breadthfirstsearch(layer+1,list)
        if self.right!=None:
            list=self.right.breadthfirstsearch(layer+1,list)
        return list


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

    def display(self):
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
            lines, n, p, x = self.left.display()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right.display()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left.display()
        right, m, q, y = self.right.display()
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


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, d):
        if self.root is None:
            self.root = Node(d)
        else:
            self.root.insert(d)

    def search(self, d):
        if self.root is not None:
            return self.root.search(d)
        else:
            return False

    def preorder(self):
        if self.root is not None:
            self.root.preorder()

    def inorder(self):
        if self.root is not None:
            self.root.inorder()

    def postorder(self):
        if self.root is not None:
            self.root.postorder()

    def breadthfirstsearch(self):
        if self.root is not None:
            return self.root.breadthfirstsearch()

    def delete(self, d):
        if self.root is not None:
            self.root = self.root.delete(d)

    def __str__(self):
        if self.root is not None:
            tree = self.root.display()[0]
            string = ""
            for branch in tree:
                string += branch + "\n"
            return string
        else:
            return "Empty"




nums = [20, 5, 3, 2, 1, 4, 6, 7, 20, 11, 35,
        25, 21, 45, 40, 36, 38, 50, 48, 60]
bst = BinarySearchTree()
for i in nums:
    bst.insert(i)

print(bst)






