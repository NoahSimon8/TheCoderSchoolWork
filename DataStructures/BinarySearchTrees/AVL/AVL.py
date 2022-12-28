from random import*


class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None
        self.height = 0

    def search(self, d):
        if d == self.data:
            return self.data
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
        # print("Balance: ", self.calc_balance())
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

    def insert(self, d):
        if d <= self.data:
            if self.left is None:
                self.left = Node(d)
            else:
                self.left = self.left.insert(d)
        else:
            if self.right is None:
                self.right = Node(d)
            else:
                self.right = self.right.insert(d)
        return self.insert_rebalance(d)

    def balance_parent(self, count):
        if count > 0:
            self.left = self.left.balance_parent(count-1)
        return self.delete_rebalance()

    def bal_par(self):
        if self.left is None:
            return self.delete_rebalance()
        self.left = self.left.bal_par()
        return self.delete_rebalance()

    def bal_par2(self):
        if self.left is None:
            return [self, self.right]
        nodes = self.left.bal_par2()
        self.left = nodes[1]
        tree = self.delete_rebalance()
        nodes[1] = tree
        return nodes

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

                    nodes = self.right.bal_par2()
                    self.right = nodes[1]
                    cur = nodes[0]

                    cur.right = self.right
                cur.left = left_tree

                return cur.delete_rebalance()
        if d < self.data:
            if self.left is None:
                return self
            self.left = self.left.delete(d)
        else:
            if self.right is None:
                return self
            self.right = self.right.delete(d)
        return self.delete_rebalance()

    def delete_rebalance(self):
        self.height = self.calc_height()
        balance = self.calc_balance()
        if balance == 2 and self.left.calc_balance() >= 0:      # rotate RIGHT
            return self.rotate_right()
        elif balance == 2 and self.left.calc_balance() < 0:     # rotate LEFT, RIGHT
            self.left = self.left.rotate_left()
            return self.rotate_right()
        elif balance == -2 and self.right.calc_balance() <= 0:  # rotate LEFT
            return self.rotate_left()
        elif balance == -2 and self.right.calc_balance() > 0:   # rotate RIGHT, LEFT
            self.right = self.right.rotate_right()
            return self.rotate_left()
        return self

    def insert_rebalance(self, d):
        self.height = self.calc_height()
        balance = self.calc_balance()
        if balance == 2 and d <= self.left.data:        # rotate RIGHT
            return self.rotate_right()
        elif balance == 2 and d > self.left.data:       # rotate LEFT, RIGHT
            self.left = self.left.rotate_left()
            return self.rotate_right()
        elif balance == -2 and d > self.right.data:     # rotate LEFT
            return self.rotate_left()
        elif balance == -2 and d <= self.right.data:    # rotate RIGHT, LEFT
            self.right = self.right.rotate_right()
            return self.rotate_left()
        return self

    @staticmethod
    def get_height(root):
        if root is None:
            return -1
        return root.height

    def calc_height(self):
        left_sub = self.get_height(self.left)
        right_sub = self.get_height(self.right)
        return max(left_sub, right_sub) + 1

    def calc_balance(self):
        left_sub = self.get_height(self.left)
        right_sub = self.get_height(self.right)
        return left_sub - right_sub

    def rotate_right(self):
        left_child = self.left
        self.left = left_child.right
        left_child.right = self
        self.height = self.calc_height()
        left_child.height = left_child.calc_height()
        return left_child

    def rotate_left(self):
        right_child = self.right
        self.right = right_child.left
        right_child.left = self
        self.height = self.calc_height()
        right_child.height = right_child.calc_height()
        return right_child


class AVLTree():
    def __init__(self):
        self.root = None

    def insert(self, d):
        if self.root is None:
            self.root = Node(d)
        else:
            self.root = self.root.insert(d)

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

    def delete(self, d):
        if self.root is not None:
            self.root = self.root.delete(d)
            if self.root is not None:
                self.root = self.root.delete_rebalance()

    def __str__(self):
        if self.root is not None:
            tree = self.root.display()[0]
            string = ""
            for branch in tree:
                string += branch + "\n"
            return string
        else:
            return "Empty"

#
avl = AVLTree()




nums=[]
for i in range(5000):
    num=randint(0,9999)
    nums.append(num)
for i in nums:
    avl.insert(i)


for i in nums:
    if randint(0,1)==1:
        avl.delete(i)


print(avl)
# print(avl.search(622))