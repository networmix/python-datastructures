from . import helpers


class SinglyLinkedListNode(object):
    """
    A node for a SinglyLinkedList
    Each node contains a data field ("_value")
    and a reference ("_next") to the next node in the list.
    """

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


class SinglyLinkedList(object):
    """
    A linked list is a linear data structure, in which
    the elements are not stored at contiguous memory locations.
    In simple words, a linked list consists of nodes where each node contains a data field
    and a reference(link) to the next node in the list.
    """

    def __init__(self):
        self._head = None
        self._tail = None
        self._next = None
        self._len = 0

    def __len__(self):
        return self._len

    def __iter__(self):
        next_elt = self._head
        while next_elt:
            tmp_next_elt = next_elt
            next_elt = next_elt.get_next()
            yield tmp_next_elt

    def __next__(self):
        while self._next:
            tmp_next_elt = self._next
            self._next = self._next.get_next()
            return tmp_next_elt
        raise StopIteration

    def __str__(self):
        list_elements = [str(elt.get_value()) for elt in self]
        return f"{list_elements}"

    def _append(self, node):
        if not self._head:
            self._head = node
            self._tail = node
            self._next = node
            self._len += 1
        else:
            self._tail.set_next(node)
            self._tail = node
            self._len += 1

    def _pop(self):
        if self._len == 0:
            raise IndexError
        prev = None
        cur = self._head
        for node in self:
            prev = cur
            cur = node
        prev.set_next(None)
        ret = self._tail
        self._tail = prev
        self._len -= 1
        return ret

    def pop(self):
        return self._pop().get_value()

    def append(self, value):
        self._append(SinglyLinkedListNode(value))

    def reverse(self):
        if self._len == 0:
            return self
        prev = None
        cur = self._head
        nxt = self._head.get_next()
        self._head, self._tail = self._tail, self._head
        while cur:
            cur.set_next(prev)
            prev = cur
            cur = nxt
            if nxt:
                nxt = nxt.get_next()
        return self
