class Node:
    value = 0 # making object attributes
    next = None
    def __init__(self, value, last): # constructor of node
        self.value = value
        self.next = last


def push(value, last): # Push: add values to the stack
    newNode = Node(value, last) # create new node, initialize with value and last node
    print("Pushed to stack: {0}".format(value)) # tell user
    return newNode # return new last node

def pop(last):
    print("Popping from stack node: {0}".format(last.value))
    return last.next # return new last element, thus skipping the one just popped

def isEmpty(last):
    if last is None: # if last is None, the stack is empty
        return True
    else:
        return False

def popAll(last):
    while last is not None: # this function pops all values out of the stack
        last = pop(last)


stack = None
value = 0
while True:
    print("1: Push value\n"+
          "2: Pop value\n"+
          "3: Pop all values\n"+
          "4: Quit")
    choice = input("Enter choice: ")

    if choice == "1":
        value = input("Enter value to push")
        if(stack is None):
            stack = Node(value, None)
        else:
            stack = push(value, stack)
    elif choice == "2":
        emptyBool = isEmpty(stack)
        if emptyBool:
            print("No elements to push")
        else:
            stack = pop(stack)
    elif choice == "3":
        emptyBool = isEmpty(stack)
        if emptyBool:
            print("No elements to push")
        else:
            stack = popAll(stack)
    elif choice == "4":
        break