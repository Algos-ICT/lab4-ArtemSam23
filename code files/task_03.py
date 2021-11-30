from collections_for_lab4 import Stack


f = open('../inputs/input_03.txt', 'r')
output = open('../outputs/output_03.txt', 'x')
n = int(f.readline())
for i in range(n):
    s = f.readline()
    stack = Stack()
    for j in s:
        if j in '([':
            stack.push(j)
        elif not stack.is_empty():
            if j == ')':
                if stack.top.value == '(':
                    stack.pop()
                else:
                    stack.push(j)
            elif j == ']':
                if stack.top.value == '[':
                    stack.pop()
                else:
                    stack.push(j)
        else:
            stack.push()
    if stack.is_empty():
        print('YES', file=output)
    else:
        print('NO', file=output)
