


class Heaps:
    def __init__(self):
        self.array=[]

    def append(self,node):
        self.array.append(node)
        self.bubbleUp(node)

    def pop(self):
        self.array[0]=self.array[len(self.array)-1]
        self.array.pop(len(self.array)-1)
        if len(self.array)>=2:
            self.bubbleDown()

    def bubbleUp(self,node):
        pos=len(self.array)
        while node<self.array[pos//2-1]:

            if pos-1!=0:
                self.swapUP(pos,node)
            else:
                break
            pos//=2

    def bubbleDown(self):

        pos=1
        try:
            while self.array[pos-1]>self.array[pos*2-1] or self.array[pos-1]>self.array[pos*2]:
                # left
                    if self.array[pos*2-1]<=self.array[pos*2]:
                        self.swapDOWN(pos*2,self.array[pos*2-1])
                        pos*=2

                    #right
                    else:
                        self.swapDOWN(pos*2+1,self.array[pos*2])
                        pos=pos*2+1
                    if pos*2>len(self.array):
                        break
        except:
            pass



    def swapUP(self,pos,node):
        self.array[pos - 1] = self.array[pos // 2 - 1]
        self.array[pos//2-1]=node

    def swapDOWN(self,pos,node):
        self.array[pos - 1] = self.array[pos // 2 - 1]
        self.array[pos // 2 - 1] = node


    def peak(self):
        return self.array[0]


    def display(self,cur):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        try:
            self.array[cur*2]

        except:
            try:
                self.array[cur * 2-1]
            except:
                line = '%s' % self.array[cur-1]
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

        # Only left child.
        try:
            self.array[cur * 2]
        except:
            lines, n, p, x = self.display(cur*2)


            s = '%s' % self.array[cur-1]
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        try:
            self.array[cur * 2-1]

        except:
            lines, n, p, x = self.display(cur*2+1)

            s = '%s' % self.array[cur-1]
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.display(cur*2)
        right, m, q, y = self.display(cur*2+1)
        s = '%s' % self.array[cur-1]
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
        if self.array!=[]:
            tree = self.display(1)[0]
            string = ""
            for branch in tree:
                string += branch + "\n"
            return string

        else:
            return "Empty"




H=Heaps()
H.append(10)
H.append(15)
H.append(35)
H.append(45)
H.append(55)
H.append(65)
H.append(75)
H.append(95)
H.append(105)
H.append(115)
H.append(125)
H.append(135)
H.append(145)
H.append(155)
H.append(165)
H.append(1)
H.append(2)
H.append(3)
H.append(4)
H.append(5)
H.append(6)
H.append(7)
H.append(8)
H.append(9)
H.append(11)
H.append(12)
H.append(13)
H.append(14)
H.append(15)


print(H.array)
print(H)
for i in range(len(H.array)//2):
    H.pop()
print(H)
print(H.peak())