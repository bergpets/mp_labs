class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, value):
        self.put(key, value)
    
    def put(self, key, value):
        self.root = self._put(self.root, key, value)
    
    def _put(self, node, key, value):
        if node is None:
            return Node(key, value)
        if key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        else:
            node.value = value
        return node
    
    def get(self, key):
        node = self._get(self.root, key)
        if node is None:
            raise KeyError(key)
        return node.value
    
    def _get(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node
        elif key < node.key:
            return self._get(node.left, key)
        else:
            return self._get(node.right, key)
    
    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        return True
    
    def __iter__(self):
        yield from self._traverse(self.root)
    
    def _traverse(self, node):
        if node is not None:
            yield from self._traverse(node.left)
            yield node.key
            yield from self._traverse(node.right)
            
            
            