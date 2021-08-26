import random
from typing import List, Iterator


class Node:
    """ 单向链表节点 """

    def __init__(self, data: any):
        self._data = data
        self._next = None

    def get_data(self):
        return self._data

    def set_next(self, node):
        self._next = node

    def next(self):
        return self._next


class TreeNode:
    """ 二叉树节点 """

    def __init__(self, data: any):
        self.__data = data
        self.__left = None  # 左子树
        self.__right = None  # 右子树

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right


class LinkedList:
    """ 简单的链表实现 """

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def add(self, data: any):
        node = Node(data)
        if self.__head is None:
            self.__head = node
            self.__tail = self.__head
            self.__size += 1
            return
        self.__tail.set_next(node)
        self.__tail = node
        self.__size += 1

    def pop(self) -> any:
        node = self.__head
        self.__head = self.__head.next()
        node.set_next(None)
        self.__size -= 1
        return node.get_data()

    def size(self) -> int:
        return self.__size

    def __str__(self):
        if self.__size == 0:
            return '[]'
        node = self.__head
        s = '[ '
        while node is not None:
            s += str(node.get_data())
            node = node.next()
            if node:
                s += ' => '
        s += ' ]'
        return s


class Stack:
    """
    后进先出数据结构
    """

    def __init__(self):
        self.__items = []

    def push(self, item: any):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[len(self.__items)]

    def size(self) -> int:
        return len(self.__items)

    def is_empty(self) -> bool:
        return self.__items == []

    def __iter__(self):
        copy = self.__items.copy()
        copy.reverse()
        return iter(copy)


class Bag:
    """
    Bag背包结构，是一种不支持删除元素的线性结构，它的目的是帮助用例
    收集元素并迭代遍历所有元素，迭代顺序不确定且和用例无关
    """

    def __init__(self):
        self.__container = []

    def add(self, item):
        self.__container.append(item)

    def __iter__(self):
        return RandomListIterator(self.__container.copy())


class RandomListIterator(Iterator):
    # 随机迭代器
    def __init__(self, ls: List):
        self.__list = ls

    def __next__(self):
        if len(self.__list) > 0:
            i = random.randint(0, len(self.__list) - 1)
            return self.__list.pop(i)
        else:
            raise StopIteration


if __name__ == '__main__':
    lklist = LinkedList()
    lklist.add('Mike')
    lklist.add('Zhangsan')
    lklist.add('Lisi')
    lklist.add('Wangwu')
    print(lklist.pop())
    print(lklist)
    print(lklist.size())

    stack = Stack()
    stack.push("A")
    stack.push("B")
    stack.push("C")
    for x in stack:
        print(x)
    print('========================')
    while not stack.is_empty():
        print(stack.pop())

    bag = Bag()
    bag.add('dlskjs')
    bag.add("dlsooo")
    bag.add("klksdkok")
    bag.add("ooskkdoso")
    for x in bag:
        print(x)
