class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def __str__(self):
        return f"{self.head.data}\n{self.head.next_node.data}\n{self.tail.data}"

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        if self.head is None and self.tail is None:
            self.head = Node(data, self.tail)
        elif self.head is not None and self.tail is None:
            self.tail = Node(data, self.tail)
            self.head.next_node = self.tail
        else:
            next_node = None
            self.tail = Node(data, next_node)

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        pass
