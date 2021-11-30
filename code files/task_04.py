from collections_for_lab4 import Stack


def parse_brackets(s):
    stack = Stack()
    index = None
    for i in range(len(s)):
        if s[i] in '([{}])':
            if s[i] in '}])':
                if stack.is_empty() or stack.top.value[0] + s[i] not in ('()', '[]', '{}'):
                    index = i
                    break
                else:
                    stack.pop()
            else:
                stack.push((s[i], i))
    if index is not None:
        return index + 1
    if stack.is_empty():
        return 'Success'
    # так как не можем обратиться к нулевому элементу стэка
    while stack.top.previous_item.value is not None:
        stack.pop()
    return stack.top.value[1] + 1


f = open('../inputs/input_04.txt', 'r')
output = open('../outputs/output_04.txt', 'w')
lines = f.readlines()
for line in lines:
    print(parse_brackets(line), file=output)
