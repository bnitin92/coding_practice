# Insert an item at the bottom of a stack

def insertBottom(stack, ele):

    if len(stack) == 0:
        stack.append(ele) # push the element
    else:
        temp = stack.pop() # temp stores at every recursive instance
        insertBottom(stack, ele) # think the recursive step as if you are going to be inside
        stack.append(temp) # appends at every recursive instance

    #print(stack) # will print every time
    return stack

print(insertBottom([2,3,4,5,6], 1))