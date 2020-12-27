class Stack():
    def __init__(self):
        self.array = list()

    def push(self, value: int):
        self.array.append(value)

    def pop(self) -> int:
        value = self.array[-1]
        self.array = self.array[0:-1]
        return value


def main():
    input = '1 2 + 3 4 - *'
    arr = input.split()
    stack = Stack()
    for i in arr:
        if i == '+':
            right = stack.pop()
            left = stack.pop()
            value = left + right
            stack.push(value)
        elif i == '-':
            right = stack.pop()
            left = stack.pop()
            value = left - right
            stack.push(value)
        elif i == '*':
            right = stack.pop()
            left = stack.pop()
            value = left * right
            stack.push(value)
        else:
            stack.push(int(i))
    return stack.array


if __name__ == '__main__':
    arr = main()
    assert arr[0] == -3