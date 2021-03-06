"""Binary tree module"""

from queue import Queue


class BSTNode:
    """
    Node obj

    val: node value
    left: left node
    right: right node
    """

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return f'-{self.val}-'


class BinarySearchTree:
    """Binary Search Tree"""

    def __init__(self, array=None):
        self.root_node = None
        self.size = 0

        # add nodes from array
        if array is not None:
            for val in array:
                self.insert(val)

    def __str__(self):
        return str(self.to_array())

    def insert(self, val):
        """Add new node"""

        if self.root_node is None:
            self.root_node = BSTNode(val)
        else:
            self._insert(self.root_node, val)

        self.size += 1

    def _insert(self, node, val):
        if node.val == val:
            raise ValueError(f"duplicate value {val}")

        if node.val < val:
            if node.right is None:
                node.right = BSTNode(val)
            else:
                self._insert(node.right, val)
        else:
            if node.left is None:
                node.left = BSTNode(val)
            else:
                self._insert(node.left, val)

    def contains(self, val):
        """Find node by value"""

        current_node = self.root_node

        while current_node is not None:
            if current_node.val == val:
                return True
            elif current_node.val < val:
                current_node = current_node.right
            else:
                current_node = current_node.left

        return False

    def remove(self, val):
        """Remove node"""

        current_node = self.root_node
        parent_node = None
        node_to_remove = None

        # find node to remove
        while current_node is not None:
            if current_node.val == val:
                node_to_remove = current_node
                break
            elif current_node.val < val:
                parent_node = current_node
                current_node = current_node.right
            else:
                parent_node = current_node
                current_node = current_node.left

        if node_to_remove is None:
            raise ValueError(f"can't find node to remove {val}")

        # case 1: node has no children
        # just remove it
        if node_to_remove.left is None and node_to_remove.right is None:
            if node_to_remove.val == parent_node.left.val:
                parent_node.left = None
            else:
                parent_node.right = None

            self.size -= 1
            return

        # case 2: node has one child
        # just replace removed node with it's child
        if node_to_remove.left is None or node_to_remove.right is None:
            if parent_node.left is node_to_remove:
                parent_node.left = node_to_remove.left if node_to_remove.left is not None else node_to_remove.right
            else:
                parent_node.right = node_to_remove.left if node_to_remove.left is not None else node_to_remove.right
            self.size -= 1
            return

        # case 3: node has two children
        # find the min node in the right subtree
        # replace removed node value with the min node val
        # remove the min node
        min_leaf = node_to_remove.right
        min_leaf_parent = node_to_remove

        while True:
            if min_leaf.left is None:
                break
            else:
                min_leaf_parent = min_leaf
                min_leaf = min_leaf.left

        node_to_remove.val = min_leaf.val
        min_leaf_parent.left = None
        self.size -= 1

    def clear(self):
        """Remove all nodes"""

        self.root_node = None
        self.size = 0

    def to_array(self):
        """Returns tree in array representation"""

        if self.root_node is None:
            return []

        ar = []
        q = Queue()

        current_node = self.root_node

        q.enqueue(current_node)
        while not q.empty():
            node = q.dequeue()
            ar.append(node.val)
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)

        return ar

    def traversal_in_order(self, action):
        """
        InOrder traversal, the nodes would be sorted in numerical order
        from smallest to largest
        """

        self._trav_in(self.root_node, action)

    def _trav_in(self, node, action):
        if node is not None:
            self._trav_in(node.left, action)
            action(node)
            self._trav_in(node.right, action)

    def traversal_pre_order(self, action):
        """PreOrder traversal"""

        self._trav_pre(self.root_node, action)

    def _trav_pre(self, node, action):
        if node is not None:
            action(node)
            self._trav_pre(node.left, action)
            self._trav_pre(node.right, action)

    def traversal_post_order(self, action):
        """
        PostOrder traversal, PostOrder traversals are often used to delete an entire tree,
        such as in programming languages where each node must be freed, or to delete subtrees
        """

        self._trav_post(self.root_node, action)

    def _trav_post(self, node, action):
        if node is not None:
            self._trav_post(node.left, action)
            self._trav_post(node.right, action)
            action(node)

    def root(self):
        """Root node"""

        if self.root_node is None:
            raise ValueError("no root node")

        return self.root_node

    def count(self):
        """Number of nodes"""

        return self.size

    def print(self):
        self._print_node(self.root_node, 0)

    def _print_node(self, node, depth):
        val = f"{node.val}"
        print(val.rjust(len(val) + depth * 5, " "))

        if node.left is not None:
            self._print_node(node.left, depth+1)

        if node.right is not None:
            self._print_node(node.right, depth+1)
    """
    (4)
    |
    `---(1)
    |   |
    |   `---(0)
    |
    `---(6)
        |
        `---(5)
        |
        `---(12)
            |
            `---(7)
            |   |
            |   `---(9)
            |
            `---(13)
    """

if __name__ == "__main__":
    pass

    some_values = [4, 1, 6, 0, 12, 7, 13, 5, 9]
    bst_tree = BinarySearchTree(some_values)
    bst_tree.print()
    # bst_tree.traversal_pre_order(print)
    # bst_tree.traversal_post_order(print)
    # bst_tree.traversal_in_order(print)
    # print(bst_tree)
    # print(bst_tree.count())
    # bst_tree.remove(6)
    # print(bst_tree)
    # print(bst_tree.count())
    # print(f"root - {bst_tree.root()}")
    # print(f"number of nodes - {bst_tree.count()}")
    # print(f"found - {bst_tree.contains(1)}")
    # print(bst_tree.count())
    # print(bst_tree.to_array())
    # bst_tree.insert(44)
    # bst_tree.insert(23)
    # print(f"number of nodes - {bst_tree.count()}")
    # print(bst_tree)
    # bst_tree.remove(44)
    # bst_tree.remove(1)
    # print(bst_tree)

