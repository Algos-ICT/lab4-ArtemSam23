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
