# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

class MinStack:
    def __init__(self):
        self.minstack = []
        self.stack = []
    def push(self, val: int):
        self.stack.append(val)
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)
    def pop(self):
        self.stack.pop()
        self.minstack.pop()
    def top(self)-> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minstack[-1]

# Testing
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
test1 = minStack.getMin()
# minStack.getMin() // return -3
assert test1 == -3, f"Value expected to be -3 but is instead {test1}."

minStack.pop()

# minStack.top()    // return 
test2 = minStack.top()
assert test2 == 0, f"Value expected to be 0 but is instead {test2}."

# minStack.getMin() // return -2
test3 = minStack.getMin()
assert test3 == -2, f"Value expected to be -2 but is instead {test3}."

