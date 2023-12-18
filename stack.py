

stack = []


# append is the equivalent of push
stack.append(1)


stack.append(2)


stack.append(3)

# pop from the end
print(stack.pop())

def peek(stack):
  return stack[-1]

peek(stack)


print(stack.pop())
print(stack.pop())
# NOTE: we just flipped our numbers, we added 1,2,3 but then receieved 3,2,1. 

# this is a stack with all 3 operations, push, pop and peek. 

# NOTE: this is LIFO. Last in first out. 