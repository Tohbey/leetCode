class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        else:
            return False



res = MyStack()

res.push(1)
res.push(2)
print(res.top())
print(res.pop())
print(res.empty())