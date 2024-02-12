import BST
import AVLTreeMap

bst = BST.BinarySearchTree()
bst.insert(2)
bst.insert(1)
bst.insert(3)
bst.insert(4)
bst.insert(5)
print(bst.get_total_height())

numbers = [17, 4, 1, 20, 9, 23, 18, 34]
numbers_tree = BST.BinarySearchTree.serialize(root=numbers)
print(numbers_tree.in_order())
print(testing.get_total_height(17))
