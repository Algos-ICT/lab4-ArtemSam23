"""Library for Lab 4"""


def print_arr(arr: list, file=None):
    print(' '.join(map(str, arr)), file=file)


# for task 1
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


# for task 2
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


# class for item of Queue
class QueueItem:

    def __init__(self, value=None, previous_item=None, next_item=None):
        self.value = value
        self.previous_item = previous_item
        self.next_item = next_item

    def __str__(self):
        return str(self.value)


# for task 5
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


# for tasks 6, 7
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


# for task 8
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


# for task 9
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


# tests for classes
def _test_stack_with_min_max():

    stack = StackWithMaxMin()
    while True:
        i = input()
        if i == 'quit':
            break
        elif i == 'print':
            print(stack)
        elif i[:4] == 'push':
            stack.push(int(i[5:]))
        elif i[:3] == 'pop':
            print(stack.pop())
        elif i[:3] == 'max':
            print(stack.get_max())
        elif i[:3] == 'min':
            print(stack.get_min())


def _test_stack_with_calculator():

    stack = StackWithCalculator()
    while True:
        i = input()
        if i == 'quit':
            break
        elif i == 'print':
            print(stack)
        elif i[:4] == 'push':
            stack.push(i[5:])


def _test_queue_with_mid():
    que_with_mid = QueueWithMid()
    while True:
        i = input()
        if i == 'quit':
            break
        elif i[0] == '+':
            que_with_mid.push(i[2:])
        elif i[0] == '*':
            que_with_mid.insert_in_the_mid(i[2:])
        elif i[0] == '-':
            print(que_with_mid.pop())
