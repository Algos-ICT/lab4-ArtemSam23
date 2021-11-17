from pathlib import Path


def main(
        path_to_inputs=Path('../inputs/input_11.txt'),
        path_to_outputs=Path('../outputs/output_11.txt')):

    from collections_for_lab4 import Queue
    _input = open(path_to_inputs, mode='r')
    output = open(path_to_outputs, mode='w')

    # n - количество клиентов, m - количество справок
    n, m = map(int, _input.readline().split())

    queue = Queue()
    for k in map(int, _input.readline().split()):
        queue.push(k)

    while not queue.is_empty() and m > 0:
        m -= 1
        k = queue.pop() - 1
        if k > 0:
            queue.push(k)

    while not queue.is_empty():
        print(queue.pop(), end=' ', file=output)


if __name__ == '__main__':
    main()
