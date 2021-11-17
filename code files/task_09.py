from pathlib import Path


def main(
        path_to_inputs=Path('../inputs/input_09.txt'),
        path_to_outputs=Path('../outputs/output_09.txt')):

    from collections_for_lab4 import QueueWithMid
    _input = open(path_to_inputs, mode='r')
    output = open(path_to_outputs, mode='w')

    n = int(_input.readline())

    queue = QueueWithMid()
    for _ in range(n):
        i = _input.readline()
        if i[0] == '+':
            queue.push(int(i[2:]))
        elif i[0] == '*':
            queue.insert_in_the_mid(int(i[2:]))
        elif i[0] == '-':
            print(queue.pop(), file=output)


if __name__ == '__main__':
    main()
