

class Node:
    def __init__(self,d=None):
        self.data = d
        self.left = None
        self.right = None


    def insert(self, d):
        if self.data==None:
            self.data=d
        else:
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

    def search(self,d):
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



    def delete(self, d):
        #traversing the tree
        current = bst
        root = None
        while True:
            if current.data == d:
                break
            root=current
            if d < current.data:
                current = current.left
            elif d > current.data:
                current = current.right

        #weather current is to the left or right of its root
        if root==None:
            if current.right!=None:
                pos="TopRight"
            elif current.left!=None:
                pos="TopLeft"
            else:
                pos="Nothing"
        elif current.data > root.data:
            pos = "right"
        else:
            pos = "left"

        # 0-1 child
        if current.right==None or current.left==None:
            if current.right!=None:
                if pos=="TopRight":
                    self.data=self.right.data
                    self.left=self.right.left
                    self.right=self.right.right
                elif pos=="TopLeft":
                    self.data=self.left.data
                    self.right=self.left.right
                    self.left=self.left.left
                elif pos=="right":
                    root.right=current.right
                else:
                    root.left=current.right
            else:
                if pos=="TopRight":
                    self.data=self.right.data
                    self.left=self.right.left
                    self.right=self.right.right
                elif pos=="TopLeft":
                    self.data=self.left.data
                    self.right=self.left.right
                    self.left=self.left.left
                elif pos=="Nothing":
                    self.data=None
                elif pos=="right":
                    root.right=current.left
                else:
                    root.left=current.left

        # 2 children
        else:
            #taverse the tree from current
            next=current.right
            if next.left==None:
                posnext="right"
                nextroot=current

            else:
                posnext="left"
                while next.left!=None:
                    nextroot=next
                    next=next.left
            #swapping stuff
            if posnext=="right":
                nextroot.right=next.right
            else:
                nextroot.left=next.right
            next.right=current.right
            next.left=current.left
            if pos=="right":
                root.right=next
            elif pos=="left":
                root.left=next
            else:
                self.data=next.data
                self.left=next.left
                self.right=next.right


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

#
# bst = Node()
# nums=[5,9,1,3,7,5,15,12,20,25,14,13,17,16,23,28,9,17,13,10]
# for i in nums:
#     bst.insert(i)
# print(bst)
# print(bst.search(1222))
# bst.delete(20)
# bst.delete(5)
# print(bst)
