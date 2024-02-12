class Node:
    def __init__(self, core):
        self.core = core  # core stem value
        self.left = None  # initializing the left and right child nodes
        self.right = None

    def insert(self, data):  # recursive function that searches and inserts a new node
        if self.core == data:
            return

        elif self.core > data:  # will keep calling function until it fills empty space
            if self.left:
                self.left.insert(data)  # inserts in the left
            else:
                self.left = Node(data)

        else:
            if self.right:
                self.right.insert(data)  # inserts in the right
            else:
                self.right = Node(data)

    def get_total_height(self):  # attempting to get the height of the node
        if self.left and self.right:
            return 1 + max(self.left.get_total_height(), self.right.get_total_height())
        elif self.left:
            return 1 + self.left.get_total_height()
        elif self.right:
            return 1 + self.right.get_total_height()
        else:
            return 1

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):  # using the function from Node class for inserting a new piece of data in the BST
        if self.root:
            self.root.insert(data)
        else:
            self.root = Node(data)

    def get_total_height(self):  # getting the sum of the heights of the nodes
        if self.root:
            return self.root.get_total_height()
        else:
            return 0

    def get_weight_balance_factor(self, root):
        if root is None:
            return True

        # get the height of each roots
        left_node = Node.get_total_height(root.left)
        right_node = Node.get_total_height(root.right)

        # if it's within -1, 0, 1... return True
        if self.get_weight_balance_factor(root.left) and self.get_weight_balance_factor(root.right):
            if (abs(left_node - right_node) <= 1):
                return True

        return False  # not balanced, return False

    def serialize(self, root):
        elements = []

        def dfs(node): # using depth first search
            if not node:
                elements.append("None") # append None to emtpy nodes
                return
            elements.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return elements

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0

        def dfs(): # deconstructing data and rebuilding it
            if vals[self.i] == "None":
                self.i += 1 # next value
                return None
            node = Node(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
