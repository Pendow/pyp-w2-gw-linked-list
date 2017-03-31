from .interface import AbstractLinkedList
from .node import Node


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.start = None
        self.end = None 
        
        if elements:
            for e in elements:
                self.append(e)


    def __str__(self): 
        inner = ', '.join(str(elem) for elem in self)
        return '[{}]'.format(inner)
        

    def __len__(self):
        return self.count()

    def __iter__(self):
        node = self.start
        while node:
            yield node.elem
            node = node.next
        raise StopIteration

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError
        for idx, element in enumerate(self):
            if idx == index:
                return element
        

    def __add__(self, other):
        new_list = LinkedList(elem for elem in self)
        for e in other:
            new_list.append(e)
        return new_list

    def __iadd__(self, other):
        for e in other:
            self.append(e)
        return self

    def __eq__(self, other):
        node_self = self.start #first node from the linkedlist
        node_other = other.start
       
       #all elements are equal => same length
       #self node and other node should be equal
       #same_length = len(self) == len(other)
       
        while True:
            if not node_self and not node_other:
                return True
            
            if not bool(node_self) or not bool(node_other):
                return False
            
            if node_self.elem != node_other.elem:
                return False
 
            node_self = node_self.next
            node_other = node_other.next
            
    
    def __ne__(self,other):
        return not self.__eq__(other)


    def append(self, elem):
        if not self.start:
            self.start = Node(elem)
            self.end = self.start
        else:
            self.end.next = Node(elem) #next=None
            self.end = self.end.next
        

    def count(self):
        _count = 0
        for i in self:
            _count += 1
        return _count
            

    def pop(self, index=None):
        if index is None:
            index = len(self)-1
        
        if len(self) == 0 or index >= len(self):
            raise IndexError
            
        # pop(0)
        if index == 0:
            elem = self.start.elem
            self.start = self.start.next
            return elem
        
        prev_node = None
        node = self.start
        i = 0
        
        while True:
            if i == index:
                prev_node.next = node.next
                return node.elem
            prev_node = node
            node = node.next
            i+=1