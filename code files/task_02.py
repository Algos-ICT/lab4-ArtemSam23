from collections_for_lab4 import Queue


queue = Queue()
f = open('input_02.txt',  'r')
output = open('output_02.txt',  'x')
n = f.readline()
for i in f.readlines():
    if i[0] == '+':
        queue.push(int(i[2:]))
    else:
        print(queue.pop(), file=output)
