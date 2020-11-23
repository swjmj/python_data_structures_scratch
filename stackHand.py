class stackHand:
    current = None
    bottom = None

    def __init__(self):
        return

    def push(self, val):
        if self.current is None:
            self.current = val

        else:
            temp = stackHand()
            temp.push(self.current)
            temp.bottom = self.bottom
            self.bottom = temp
            temp = None
            self.current = val

    def printStack(self):
        print(self.current)

        if self.bottom is not None:
            self.bottom.printStack()

    def find(self, val):
        if self.current == val:
            return True
        else:
            if self.bottom is not None:
                return self.bottom.find(val)
            else:
                return False

    def pop(self, memory=None):
        if memory == None:
            memory = self.current

        if self.bottom is None:
            tempVal = self.current
            self.current = None
            return tempVal

        else:
            if self.bottom.bottom is None:
                tempVal = self.current
                self.current = self.bottom.current
                self.bottom = None
                return memory
            else:
                self.current = self.bottom.current
                return self.bottom.pop(memory)
