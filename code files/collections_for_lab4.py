# Lib for lab №4

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
    >>> stack = Stack()
    >>> stack.push('element1', 'element2')
    >>> print(stack)
    [element1, element2]
    >>> stack.pop()
    element2
    >>> stack.pop()
    element1
    >>> stack.pop()
    IndexError: pop from an empty stack
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
            raise IndexError('pop from an empty stack')
        popped_element = self.top.value
        self.top = self.top.previous_item
        return popped_element

    def __str__(self):
        return f'[{self.top}]'


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
        if data is not None:
            self.push(data)

    def push(self, *items):
        for item in items:
            self.__create_node__(item)

    def __create_node__(self, item):
        new_node = QueueItem(item, self.last)
        self.last.next_item = new_node
        self.last = new_node

    def pop(self):
        """
        pops first item, but actually pops first.next_item and returns it
        :return: str
        """

        if self.is_empty():
            raise IndexError('pop from an empty queue')

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


if __name__ == '__main__':
    d = Queue()
    s = input()
    while s != 'q':
        if s[0] == '+':
            d.push(int(s[1:]))
        else:
            d.pop()
        s = input()
