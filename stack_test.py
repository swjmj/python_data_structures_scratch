from stackHand import stackHand

a = stackHand()

a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)


a.printStack()

r = a.find(3)
print('Is the value 3 in the stack?', r)


print('Popped value', a.pop())


print('----------------------------------------------')
a.printStack()
