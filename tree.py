class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    def show(self):
        if self.left:
            self.left.show()
        print(self.data)
        if self.right:
            self.right.show()

root = Node(100)
r_left = Node(12)
r_right = Node(105)
root.left = r_left
root.right = r_right
root.show()