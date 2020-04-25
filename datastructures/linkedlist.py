from . import helpers


class Node(object):
    def __init__(self, value=None):
        self._value = value
        self._next = None

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    def get_next(self):
        return self._next

    def set_next(self, node):
        self._next = node


class SingleLinkedList(object):
    def __init__(self):
        self._head = None
        self._tail = None
        self._len = 0

    def __len__(self):
        return self._len

    def _append(self, node):
        if not self._head:
            self._head = node
            self._tail = node
            self._len += 1
        else:
            self._tail.set_next(node)
            self._tail = node
            self._len += 1

    def _traverse(self):
        queue = []
        if self._head:
            queue.append(self._head)
        while queue:
            elt = queue.pop()
            next_elt = elt.get_next()
            if next_elt is not None:
                queue.append(next_elt)
            yield elt
    
    def __str__(self):
        list_elements = [str(elt.get_value()) for elt in self._traverse()]
        return f"{list_elements}"


    def append(self, value):
        self._append(Node(value))