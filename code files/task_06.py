from collections_for_lab4 import QueueWithMinMax
from pathlib import Path

PATH_TO_INPUTS = Path('../inputs/input_06.txt')
PATH_TO_OUTPUTS = Path('../outputs/output_06.txt')
INPUT = open(PATH_TO_INPUTS, mode='r')
OUTPUT = open(PATH_TO_OUTPUTS, mode='w')


queue = QueueWithMinMax()
n = int(INPUT.readline())

if __name__ == '__main__':
    for _ in range(n):
        operation = INPUT.readline()
        if operation[0] == '+':
            queue.push(int(operation[2:]))
        elif operation[0] == '?':
            print(queue.get_min(), file=OUTPUT)
        elif operation[0] == '-':
            queue.pop()
