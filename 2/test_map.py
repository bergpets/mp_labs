from map import BinarySearchTree
bst = BinarySearchTree()
bst.put("apple", 1)
bst.put("banana", 2)
bst.put("orange", 3)

print(bst.get("apple"))
print(bst.get("banana"))
print("orange" in bst)
print("pear" in bst)

bst["apple"] = 4
print(bst.get("apple"))