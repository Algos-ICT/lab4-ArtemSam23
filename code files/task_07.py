from collections_for_lab4 import QueueWithMinMax as Dequeue, print_arr
from pathlib import Path

PATH_TO_INPUTS = Path('../inputs/input_07.txt')
PATH_TO_OUTPUTS = Path('../outputs/output_07.txt')
INPUT = open(PATH_TO_INPUTS,   mode='r')
OUTPUT = open(PATH_TO_OUTPUTS, mode='w')


def max_in_slices(size_of_data, data,  size_of_slice):
    if size_of_data is None:
        size_of_data = len(data)
    d = Dequeue()
    maxes = []
    for i in range(size_of_slice):
        d.push(data[i])
    maxes.append(d.get_max())
    for i in range(size_of_slice, size_of_data):
        d.pop()
        d.push(data[i])
        maxes.append(d.get_max())
    return maxes


if __name__ == '__main__':
    n = int(INPUT.readline())
    s = list(map(int, INPUT.readline().split()))
    m = int(INPUT.readline())
    print_arr(max_in_slices(n, s, m), OUTPUT)
