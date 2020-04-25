from .context import linkedlist

import pytest


def test_create_node():
    head = linkedlist.Node()
    assert head

def test_create_linkedlist():
    ll = linkedlist.SingleLinkedList()
    assert len(ll) == 0
    
def test_linkedlist_append():    
    test_dataset = [10, 11, 'a', 'b', None]
    ll = linkedlist.SingleLinkedList()
    for elt in test_dataset:
        ll.append(elt)
    assert len(ll) == 5
    assert str(ll) == "['10', '11', 'a', 'b', 'None']"