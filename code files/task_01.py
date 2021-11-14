from collections_for_lab4 import Stack


stack = Stack()
f = open('../inputs/input_01.txt', 'r')
output = open('../outputs/output_01.txt', 'w')
n = f.readline()
for i in f.readlines():
    if i[0] == '+':
        stack.push(int(i[2:]))
    else:
        print(stack.pop(), file=output)
