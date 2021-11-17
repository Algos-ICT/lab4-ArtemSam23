from collections_for_lab4 import StackWithCalculator as PostfixCalculator
from pathlib import Path


def main(
        path_to_inputs=Path('../inputs/input_08.txt'),
        path_to_outputs=Path('../outputs/output_08.txt')):

    _input = open(path_to_inputs, mode='r')
    output = open(path_to_outputs, mode='w')

    n = int(_input.readline())
    data = _input.readline().split()

    calculator = PostfixCalculator()
    for i in range(n):
        calculator.push(data[i])
    print(calculator.pop(), file=output)


if __name__ == '__main__':
    main()
