"""
Linked list module
"""


class LLNode:
    """
    Linked List Node

    val: node value
    next: link to next node
    """

    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return f'-{self.val}-'


class LinkedList:
    """Linked List"""

    def __init__(self, array=None):
        self.size = 0
        self.root_node = None
        self.last_node = self.root_node

        if array is not None:
            for a in array:
                self.add(a)

    def __str__(self):
        return str(self.to_array())

    def __iter__(self):
        current_node = self.root_node

        while current_node is not None:
            yield current_node.val
            current_node = current_node.next

    def __len__(self):
        return self.size

    def add(self, val):
        """Add node"""

        new_node = LLNode(val)
        if self.root_node is None:
            self.root_node = new_node
            self.last_node = new_node
        else:
            self.last_node.next = new_node
            self.last_node = new_node

        self.size += 1

    def remove(self, val):
        """Remove node"""

        prev_node = None
        current_node = self.root_node
        while current_node is not None:
            if current_node.val == val:
                if prev_node is not None:
                    prev_node.next = current_node.next

                    if current_node.next is None:
                        self.last_node = prev_node
                else:
                    self.root_node = current_node.next

                    if current_node is None:
                        self.last_node = None

                self.size -= 1
                return
            else:
                prev_node = current_node
                current_node = current_node.next

        raise ValueError(f"can't find value to remove: {val}")

    def count(self):
        return self.size

    def clear(self):
        self.root_node = None
        self.size = 0

    def contains(self, val):
        current_node = self.root_node
        while current_node is not None:
            if current_node.val == val:
                return True
            current_node = current_node.next

        return False

    def to_array(self):
        ar = []

        current_node = self.root_node
        while current_node is not None:
            ar.append(current_node.val)
            current_node = current_node.next

        return ar

if __name__ == "__main__":
    pass
    # linked_list = LinkedList([1, 2, 3, 4, 5, 6, 33, 44])
    # print(linked_list.contains(2))
    # print(linked_list.contains(24))
    # print(linked_list)
    # print(len(linked_list))

    # for n in linked_list:
    #     print(n)

    # print(linked_list.count())
    # linked_list.add(7)
    # print(linked_list.to_array())
    # linked_list.remove(7)
    # print(linked_list.to_array())
    # linked_list.remove(5)
    # print(linked_list.to_array())
    # linked_list.remove(1)
    # print(linked_list.to_array())
    # linked_list.remove(3)
    # linked_list.remove(2)
    # linked_list.remove(4)
    # print(linked_list.to_array())
    # linked_list.remove(6)
    # print(linked_list.to_array())
    pass