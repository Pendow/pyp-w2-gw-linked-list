class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next
        

    def __str__(self):
        return "{} > {}".format(repr(self), repr(self.next) if self.next else '/')

    def __eq__(self, other):
       return self.elem == other.elem and self.next == other.next

    def __repr__(self):
        return "Node({})".format(self.elem)
