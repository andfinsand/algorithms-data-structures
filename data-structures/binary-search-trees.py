# Create a binary tree with nodes

class Node():
    def __init__(self , value):
        self.value = value
        self.left = None
        self.right = None

class Tree():
    def __init__(self, value):
        self.root = Node(value)

    def add(self, value): # myTree.add(5)
        newNode = Node(value)   # newNode with a value of 5
        runner = self.root  # runner is the root of my tree
        while runner:   # while I have a runner present (should never break on its own)
            if newNode.value < runner.value:    # if this new value is less than (5<7)
                if runner.left == None:
                    runner.left = newNode
                    return self
                else:
                    runner = runner.left # runner stops here and loops back to line 17.
            else:
                if runner.right == None:
                    runner.right = newNode
                    return self
                else:
                    runner = runner.right
    def contains(self, value):
        runner = self.root
        while runner:
            if value == runner.value:
                return True
            else:
                if value < runner.value:
                    if runner.left == None:
                        return False
                    else:
                        runner = runner.left
                else:
                    if runner.right == None:
                        return False
                    else:
                        runner = runner.right

myTree = Tree(7)

print(myTree.add(4).add(2).add(8).contains(1))


print(myTree.root.right.value)