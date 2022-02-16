class MyQueue:

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop(0)
        

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        else:
            return False

res = MyQueue()

res.push(1) 
res.push(2) 
print(res.peek())
print(res.pop())
print(res.empty())
print(res.stack)