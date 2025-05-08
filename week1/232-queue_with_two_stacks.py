
# Key Idea:
# Using two stacks: stack_in for push and stack_out: used for pop and peek
# When stack_out is empty, we transfer all elements from stack_in to stack_out to reverse the order
# (so the front of the queue is at the top of stack_out)
class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
        self.len = 0


    def push(self, x: int) -> None:
        self.stack_in.append(x)
        self.len += 1

    def pop(self) -> int | None:
        self._transfer()

        if self.empty():
            return None

        self.len -= 1
        return self.stack_out.pop()


    def peek(self) -> int | None:
        self._transfer()
        if self.empty():
            return None
        return self.stack_out[-1]


    def empty(self) -> bool:
        return self.len == 0

    def _transfer(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
