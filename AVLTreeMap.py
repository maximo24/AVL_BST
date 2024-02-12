class Node:
    def __init__(self, key = None, value = None):
        self.left = None
        self.right = None
        self.key = key
        self.value = value

class AVLTreeMap:

    def __init__(self):
        self.node = None
        self.height = 0 # AVL tree maps need to be balanced
        self.balance = 0

    def get(self, key): # function to check if key is in the map
        n = Node(key)

        if self.node == None: # initial node is null
            return None

        elif key == self.node.key: # found key, return value
            return self.node.value

        elif key < self.node.key: # keep checking left node for key until found or null
            if self.node.left is None:
                return None
            else:
                self.node.left.get(key)

        elif key > self.node.key: # keep checking right node until found or null
            if self.node.right is None:
                return None
            else:
                self.node.right.get(key)

    def put(self, key, value):
        # Create a new node
        n = Node(key, value) # create a node that stores a key and a value

        if  self.node == None: # if current node is empty, start setting the tree map up
            self.node = n
            self.node.left = AVLTreeMap()
            self.node.right = AVLTreeMap()

        elif key < self.node.key: # find an open spot and insert it on the left side (value is lesser)
            self.node.left.insert(key, value)

        elif key > self.node.key: # find an open spot and insert it on the left side (value is more)
            self.node.right.insert(key, value)




