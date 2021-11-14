from collections_for_lab4 import StackWithMaxMin


def run_test(a):
    output = open('outputs/output_05.txt', 'w')
    stack = StackWithMaxMin()
    for i in a:
        if i[:4] == 'push':
            stack.push(int(i[5:]))
        elif i[:3] == 'pop':
            stack.pop()
        elif i[:3] == 'max':
            print(stack.get_max(), file=output)
    output.close()


f = open('inputs/input_05.txt', 'r')
n = int(f.readline())
run_test([f.readline() for _ in range(n)])
