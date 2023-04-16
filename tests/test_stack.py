"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


# @pytest.fixture()
# def item_pc():
#     return Item("ПК", 15000, 2)
class TestStack(unittest.TestCase):
    node = Node(5, 6)
    stack = Stack()
    stack.push(10)


    # Внутри пишем нужное количество методов (функций)
    def test_stack_node_init(self):
        # Пишем нужное количество проверок
        self.assertEqual(TestStack.node.data, 5)
        self.assertEqual(TestStack.node.next_node, 6)

    def test_stack_stack_init(self):
        # Пишем нужное количество проверок
        self.assertIsInstance(TestStack.stack.top, Node)
        self.assertIsInstance(TestStack.stack, Stack)

    def test_stack_push_pop(self):
        self.stack.push(8)
        self.stack.push(6)
        self.stack.pop()
        self.assertEqual(TestStack.stack.top.data, 8)
        self.assertEqual(TestStack.stack.top.next_node.data, 10)


