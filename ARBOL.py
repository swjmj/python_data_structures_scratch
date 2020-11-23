class ARBOL:
    value = None
    left = None
    right = None

    def __init__(self, value):
        self.value = value

    def insert(self, num):
        if num < self.value:
            if self.left == None:
                self.left = ARBOL(num)
            else:
                self.left.insert(num)
        else:
            if self.right == None:
                self.right = ARBOL(num)

            else:
                self.right.insert(num)

    def printTreeIn(self):
        if self.left != None:
            self.left.printTreeIn()
        if self.value is not None:
            print(self.value)

        if self.right != None:
            self.right.printTreeIn()

    def printTreePre(self):
        if self.value is not None:
            print(self.value)

        if self.left != None:
            self.left.printTreePre()

        if self.right != None:
            self.right.printTreePre()

    def printTreePost(self):
        if self.right != None:
            self.right.printTreePost()

        if self.value is not None:
            print(self.value)

        if self.left != None:
            self.left.printTreePost()

    def search(self, num):
        if self.value == num:
            return True
        elif self.value > num:
            if self.left is None:
                return False
            else:
                return self.left.search(num)
        elif self.value < num:
            if self.right is None:
                return False
            else:
                return self.right.search(num)
