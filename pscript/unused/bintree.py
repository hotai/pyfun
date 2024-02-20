class Node:
    def __init__(self, val):
        self._value = val
        self._left = None
        self._right = None

class BinaryTree:
    def __init__(self, root):
        self._root = Node(root)

    def preorder(self, start: Node, records: list):
        if start is not None:
            records.append(start._value)
            records = self.preorder(start._left, records)
            records = self.preorder(start._right, records)
        return records

    def postorder(self, start: Node, records: list):
        if start is not None:
            records = self.postorder(start._left, records)
            records = self.postorder(start._right, records)
            records.append(start._value)
        return records

    def inorder(self, start: Node, records: list):
        if start is not None:
            records = self.inorder(start._left, records)
            records.append(start._value)
            records = self.inorder(start._right, records)
        return records


def _test():
    tree = BinaryTree('+')
    assert tree._root._value == '+'
    tree._root._left = Node('*')
    tree._root._right = Node(9)
    tree._root._left._left = Node(2)
    tree._root._left._right = Node(4)
    tree_list = tree.preorder(tree._root, [])
    assert list(['+', '*', 2, 4, 9]) == tree_list
    tree_list = tree.postorder(tree._root, [])
    assert list([2, 4, '*', 9, '+']) == tree_list

if __name__ == '__main__':
    _test()
    
