class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self):
        self.move()
        return self.output.pop()

    def peek(self):
        self.move()
        return self.output[-1]

    def empty(self):
        return not self.input and not self.output

    def move(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())