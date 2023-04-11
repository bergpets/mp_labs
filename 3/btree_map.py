from typing import TypeVar, Generic, Optional, List

K = TypeVar('K')
V = TypeVar('V')
C = TypeVar('C', bound=callable)


class Node(Generic[K, V]):
    def __init__(self, t: int):
        self.keys: List[K] = []
        self.values: List[V] = []
        self.children: List[Optional[Node[K, V]]] = [None] * (2 * t)
        self.parent: Optional[Node[K, V]] = None

    def is_leaf(self) -> bool:
        return self.children[0] is None


class DefaultComparator:
    def __call__(self, a, b):
        return a < b


class BTreeMap(Generic[K, V, C]):
    def __init__(self, t: int, comparator: C = DefaultComparator()):
        self.t = t
        self.comparator = comparator
        self.root: Optional[Node[K, V]] = None

    def __del__(self):
        self.clear()

    def clear(self):
        self.root = None

    def _find(self, key: K) -> (Node[K, V], int):
        node = self.root
        while node is not None:
            index = self._find_index(node.keys, key)
            if index < len(node.keys) and node.keys[index] == key:
                return node, index
            node = node.children[index]
        return None, None

    def _find_index(self, keys: List[K], key: K) -> int:
        index = 0
        while index < len(keys) and self.comparator(keys[index], key):
            index += 1
        return index

    def __getitem__(self, key: K) -> V:
        node, index = self._find(key)
        if node is None:
            raise KeyError(key)
        return node.values[index]

    def __setitem__(self, key: K, value: V):
        node, index = self._find(key)
        if node is not None:
            node.values[index] = value
            return

        node = self.root
        if node is None:
            self.root = Node(self.t)
            self.root.keys.append(key)
            self.root.values.append(value)
            return

        while not node.is_leaf():
            index = self._find_index(node.keys, key)
            node = node.children[index]

        self._insert(node, key, value)

    def _insert(self, node: Node[K, V], key: K, value: V):
        index = self._find_index(node.keys, key)
        node.keys.insert(index, key)
        node.values.insert(index, value)
        if len(node.keys) > 2 * self.t:
            self._split(node)

    def _split(self, node: Node[K, V]):
        middle = len(node.keys) // 2
        parent = node.parent
        if parent is None:
            parent = Node(self.t)
            self.root = parent
            parent.children[0] = node
            node.parent = parent

        right = Node(self.t)
        right.keys = node.keys[middle + 1:]
        right.values = node.values[middle + 1:]
        right.children = node.children[middle + 1:]
        for child in right.children:
            if child is not None:
                child.parent = right
        node.keys = node.keys[:middle]
        node.values = node.values[:middle]
        node.children = node.children[:middle + 1]

        index = self._find_index(parent.keys, right.keys[0])
        parent.keys.insert(index, right.keys[0])
        parent.values.insert(index, right.values[0])
        parent.children[index] = node
        parent.children.insert(index + 1, right)
        node.parent = parent
        right.parent = parent

        if len(parent.keys) > 2 * self.t:
            self._split(parent)

    def __contains__(self, key: K) -> bool:
        node, index = self._find(key)
        return node is not None

    def __delitem__(self, key: K):
        node, index = self._find(key)
        if node is None:
            raise KeyError(key)
        del node.keys[index]
        del node.values[index]
        if node.is_leaf() or len(node.keys) < self.t:
            self._restore(node)

    def _restore(self, node: Node[K, V]):
        if node.parent is None:
            if len(node.keys) == 0 and node.children[0] is not None:
                self.root = node.children[0]
                self.root.parent = None
            return

        parent = node.parent
        index = parent.children.index(node)

        if index > 0 and len(parent.children[index - 1].keys) > self.t:
            self._rotate_right(parent.children[index - 1], node, index - 1)
        elif index < len(parent.children) - 1 and len(parent.children[index + 1].keys) > self.t:
            self._rotate_left(node, parent.children[index + 1], index)
        else:
            if index == len(parent.children) - 1:
                node = parent
                index -= 1
            self._merge(node, parent.children[index + 1], index)

    def _rotate_right(self, left: Node[K, V], right: Node[K, V], index: int):
        node = right.children.pop(0)
        right.keys.insert(0, node.keys[0])
        right.values.insert(0, node.values[0])
        left.children.append(node.children.pop())
        if left.children[-1] is not None:
            left.children[-1].parent = left
        node.parent = left
        left.keys.append(node.keys.pop(0))