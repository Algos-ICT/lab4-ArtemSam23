# Лабораторная рабрта №4  
Стек, очередь, связанный список.

## Задача №1 - Стек
```python
# class for item of Stack
class StackItem:
    """
    value can't be None, because bottom element is None
    """

    def __init__(self, value=None):
        self.value = value
        self.previous_item = None

    def __str__(self):
        if self.value is None:
            return ''
        elif self.previous_item.value is None:
            return str(self.value)
        return f'{self.previous_item}, {self.value}'

    
class Stack:
    """
    >>> queue = Stack()
    
    >>> queue.push('element1', 'element2')
    
    >>> print(queue)
    
    [element1, element2]
    
    >>> queue.pop()
    
    element2
    
    >>> queue.pop()
    
    element1
    
    >>> queue.pop()
    
    IndexError: pop from an empty queue
    """

    def __create_node__(self, item):
        new_item = StackItem(item)
        new_item.previous_item = self.top
        self.top = new_item

    def push(self, *items):
        for item in items:
            self.__create_node__(item)

    def __init__(self, data=None):
        self.bottom = StackItem(None)
        self.top = self.bottom
        if data is not None:
            self.push(data)

    def is_empty(self):
        return self.top.value is None

    def pop(self):
        if self.is_empty():
            raise IndexError('pop from an empty queue')
        popped_element = self.top.value
        self.top = self.top.previous_item
        return popped_element

    def __str__(self):
        return f'[{self.top}]'
```

## Задача №2 - Очередь
```python
# class for item of Queue
class QueueItem:

    def __init__(self, value=None, previous_item=None, next_item=None):
        self.value = value
        self.previous_item = previous_item
        self.next_item = next_item

    def __str__(self):
        return str(self.value)


class Queue:

    def __init__(self, data=None):
        self.first = QueueItem()
        self.last = self.first
        self.len = 0
        if data is not None:
            self.push(data)

    def push(self, *items):
        for item in items:
            self.__create_node__(item)

    def __create_node__(self, item):
        new_node = QueueItem(item, self.last)
        self.last.next_item = new_node
        self.last = new_node
        self.len += 1

    def pop(self):
        """
        pops first item, but actually pops first.next_item and returns it
        :return: str
        """

        if self.is_empty():
            raise IndexError('pop from an empty queue')

        self.len -= 1

        popped_item = self.first.next_item.value

        if self.last.previous_item.value is None:
            self.first = QueueItem()
            self.last = self.first
            return popped_item

        self.first.next_item.next_item.previous_item = self.first
        self.first.next_item = self.first.next_item.next_item
        return popped_item

    def is_empty(self):
        return self.last.value is None
```

## Задача №3 - Скобочная последовательность. Версия 1
```python
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
```

## Задача №4 - Скобочная последовательность. Версия 2
```python
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
```

## Задача №5 - Стек с максимумом
```python
class StackWithMaxMin(Stack):

    def __init__(self):
        super(StackWithMaxMin, self).__init__()
        self.min = Stack()
        self.max = Stack()

    def __create_node__(self, item):

        new_item = StackItem(item)
        new_item.previous_item = self.top
        self.top = new_item

        if self.max.is_empty() or item >= int(self.max.top.value):
            self.max.push(self.top.value)

        if self.min.is_empty() or item <= int(self.min.top.value):
            self.min.push(self.top.value)

    def pop(self):

        if self.is_empty():
            raise IndexError('pop from an empty queue')
        if self.max.top.value == self.top.value:
            self.max.pop()
        if self.min.top.value == self.top.value:
            self.min.pop()
        popped_element = self.top.value
        self.top = self.top.previous_item
        return popped_element

    def get_max(self):
        return self.max.top.value

    def get_min(self):
        return self.min.top.value


def run_test(a):
    output = open('../outputs/output_05.txt', 'w')
    stack = StackWithMaxMin()
    for i in a:
        if i[:4] == 'push':
            stack.push(int(i[5:]))
        elif i[:3] == 'pop':
            stack.pop()
        elif i[:3] == 'max':
            print(stack.get_max(), file=output)
    output.close()


f = open('../inputs/input_05.txt', 'r')
n = int(f.readline())
run_test([f.readline() for _ in range(n)])
```

## Задача №6 - Очередь с минимумом
```python
class QueueWithMinMax:

    def __init__(self):
        self.stack_in = StackWithMaxMin()
        self.stack_out = StackWithMaxMin()

    def push(self, value):
        self.stack_in.push(value)

    def pop(self):
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.pop()

    def get_min(self):
        if self.stack_in.is_empty() and self.stack_out.is_empty():
            return None
        elif self.stack_out.is_empty():
            return self.stack_in.get_min()
        elif self.stack_in.is_empty():
            return self.stack_out.get_min()
        else:
            return min(self.stack_in.get_min(), self.stack_out.get_min())

    def get_max(self):
        if self.stack_in.is_empty() and self.stack_out.is_empty():
            return None
        elif self.stack_out.is_empty():
            return self.stack_in.get_max()
        elif self.stack_in.is_empty():
            return self.stack_out.get_max()
        else:
            return max(self.stack_in.get_max(), self.stack_out.get_max())

    def is_empty(self):
        return self.stack_in.is_empty() and self.stack_out.is_empty()

    def __str__(self):
        return str(self.stack_out)[::-1] + str(self.stack_in)


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
```

## Задача №7 - Максимум с движущейся последовательностью
```python
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
```

## Задача №8 - Постфиксная запись
```python
class StackWithCalculator(Stack):

    """item can be only digit or +, -, *"""
    def __create_node__(self, item):

        if item not in '+-*':
            item = int(item)
            super(StackWithCalculator, self).__create_node__(item)
        else:
            action = item
            if action == '+':
                self.top.previous_item.value += self.pop()
            elif action == '-':
                self.top.previous_item.value -= self.pop()
            elif action == '*':
                self.top.previous_item.value *= self.pop()
            # for division:
            # else:
            #     divider = self.pop()
            #     if divider != 0:
            #         self.top.value /= divider
            #     else:
            #         raise ValueError('division by zero')


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
```

## Задача №9 - Поликлиника
```python
class QueueWithMid(Queue):

    def __init__(self):

        super(QueueWithMid, self).__init__()
        self.mid = self.first

    def __create_node__(self, item):

        super(QueueWithMid, self).__create_node__(item)
        if not self.len % 2:
            self.mid = self.mid.next_item

    def pop(self):
        if self.last.previous_item.value is None:
            self.mid = self.first
        elif not self.len % 2:
            self.mid = self.mid.next_item

        return super(QueueWithMid, self).pop()

    def insert_in_the_mid(self, item):

        if self.mid.value is None:
            super(QueueWithMid, self).push(self, item)
        new_node = QueueItem(item, self.mid, self.mid.next_item)
        self.mid.next_item = new_node
        self.mid.next_item.previous_item = new_node
```

```python
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
```

## Задача №10 - Очередь в пекарню
```python
from pathlib import Path


class Customer:

    def __init__(self, s: str):
        arrival_hours, arrival_minutes, self.patience = map(int, s.split())
        self.arrival_time = 60*arrival_hours + arrival_minutes
        self.ttl = None

    def __str__(self):
        return f'{self.ttl//60} {self.ttl%60}'


def main(
        path_to_inputs=Path('../inputs/input_10.txt'),
        path_to_outputs=Path('../outputs/output_10.txt')):

    from collections_for_lab4 import QueueWithMid
    _input = open(path_to_inputs, mode='r')
    output = open(path_to_outputs, mode='w')

    # n - количество клиентов
    n = int(_input.readline())

    queue = QueueWithMid()

    # customers - это список времени уходово клиентов
    # так customers[0] - клиент, который пришел раньше всех,
    # customers[0] = ttl
    customers = ["didn't leave yet"]*n

    for i in range(n):
        # новый клиент
        # ttl (time to leave) - время ухода клиента
        new_customer = Customer(_input.readline())
        new_customer.id = i

        # Если к приходу нового клиента кто-то ушел,
        # то убираем их из очереди и записываем их время ухода (ttl)
        while queue.len > 0 and queue.first.next_item.value.ttl <= new_customer.arrival_time:
            customer_id = queue.first.next_item.value.id
            customers[customer_id] = str(queue.pop())

        # Если очередь пустая запускаем клиента,
        # его время ухода на 10 минут больше времени прихода
        if queue.is_empty():
            new_customer.ttl = new_customer.arrival_time + 10
            queue.push(new_customer)

        # Если терпение клиента меньше длины очереди,
        # то сразу записываем его время ухода = времени прихода
        elif new_customer.patience < queue.len:
            new_customer.ttl = new_customer.arrival_time
            customers[new_customer.id] = str(new_customer)

        # Если клиет готов подождать,
        # то его время ухода - это максимальное из времени ухода предидущего клиента +10
        # и его времени прихода +10
        else:
            new_customer.ttl = max(queue.last.value.ttl + 10, new_customer.arrival_time + 10)
            queue.push(new_customer)

    # Цикл, чтобы обработать, оставшихся в очереди, клиентов
    # Просто выпускаем их по одному, записывая их время ухода
    while not queue.is_empty():
        leaving_customer = queue.pop()
        customers[leaving_customer.id] = str(leaving_customer)

    print('\n'.join(customers), file=output)


if __name__ == '__main__':
    main()
```

## Задача №11 - Бюрократия
```python
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
```

## Задача №13
Использовал для решения других задач