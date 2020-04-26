from .context import linkedlist

import pytest


def test_create_singlylinkedlistnode():
    head = linkedlist.SinglyLinkedListNode()
    assert head


def test_create_linkedlist():
    ll = linkedlist.SinglyLinkedList()
    assert len(ll) == 0


def test_linkedlist_append():
    test_dataset = [10, 11, 'a', 'b', None]
    ll = linkedlist.SinglyLinkedList()
    for elt in test_dataset:
        ll.append(elt)
    assert len(ll) == 5


def test_linkedlist_pop():
    test_dataset = [10, 11, 'a', 'b', None]
    ll = linkedlist.SinglyLinkedList()
    for elt in test_dataset:
        ll.append(elt)
    assert len(ll) == 5
    assert ll.pop() == None
    assert ll.pop() == 'b'
    assert ll.pop() == 'a'
    assert ll.pop() == 11
    assert ll.pop() == 10
    ll.append(0)
    ll.append(1)
    assert ll.pop() == 1
    assert ll.pop() == 0
    assert len(ll) == 0
    with pytest.raises(IndexError):
        assert ll.pop()


def test_linkedlist_str():
    test_dataset = [10, 11, 'a', 'b', None]
    ll = linkedlist.SinglyLinkedList()
    for elt in test_dataset:
        ll.append(elt)
    assert str(ll) == "['10', '11', 'a', 'b', 'None']"


def test_linkedlist_next():
    test_dataset = [10, 11, 'a', 'b', None]
    ll = linkedlist.SinglyLinkedList()
    for elt in test_dataset:
        ll.append(elt)
    for elt in test_dataset:
        next(ll) == elt
    with pytest.raises(StopIteration):
        next(ll)


def test_linkedlist_reverse():
    test_dataset = [10, 11, 'a', 'b', None]
    ll = linkedlist.SinglyLinkedList()
    for elt in test_dataset:
        ll.append(elt)
    assert str(ll.reverse()) == "['None', 'b', 'a', '11', '10']"
