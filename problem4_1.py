class MaxStack:
    def __init__(self):
        self.data = []
        self.max_data = []

    def push(self, val):
        if self.max_data:
            self.max_data.append(max(val, self.max_data[-1]))
        else:
            self.max_data.append(val)
        self.data.append(val)

    def pop(self):
        self.data.pop()
        if self.max_data:
            self.max_data.pop()

    def max(self):
        return self.max_data[-1]

stack = MaxStack()
stack.push(10)
stack.push(30)
stack.push(20)
print(stack.max())
stack.pop()
print(stack.max())
stack.pop()
print(stack.max())
print(stack.max())
