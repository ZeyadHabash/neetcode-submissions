class MinStack:
    # we want a stack that keeps track of min element
    # but we want to maintain O(1) time for each of these functions
    # meaning we cannot search for min element
    # and we cannot insert in order bec that takes more than O(1)
    # hmmm...

    # we can use a stack and prio queue but that will cause pushing to be O(n)
    # let me just try it 
    # nvm that makes pushing AND popping both O(n)

    # lets create a minstack instead
    # everytime we push to the main stack we also push to the minstack
    # we push val to mainstack but we push the current minimum to minstack
    # I guess this should work??

    # god I hate python classes
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if len(self.stack) > 0:
            self.minStack.append(min(val, self.getMin()))
        else:
            self.minStack.append(val)
        self.stack.append(val)


    # dont need to handle empty stack here bec
    # "pop, top and getMin will always be called on non-empty stacks."
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
