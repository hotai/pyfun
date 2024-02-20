class Stack:
    def __init__(self):
        self._stack = []
    
    def push(self, elem):
        self._stack.append(elem)
    
    def pop(self):
        if len(self._stack) == 0:
            return None
        return self._stack.pop()
    
    def peek(self):
        if len(self._stack) == 0:
            return None
        return self._stack[-1]


def _test():
    stack1 = Stack()
    stack1.push('a')
    stack1.push('b')
    stack1.push('c')
    stack1.push('d')
    assert stack1.pop() == 'd'
    assert stack1.peek() == 'c'
    assert stack1.pop() == 'c'
    assert stack1.peek() == 'b'
    stack1.pop()
    assert stack1.pop() == 'a'


if __name__ == '__main__':
    _test()
