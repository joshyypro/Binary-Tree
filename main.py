class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class DegenerateBinaryTree:
  def __init__(self):
    self.head = None

  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      return
    curr = self.head
    while curr.right is not None:
      curr = curr.right
    curr.right = new_node

  def prepend(self, value):
    new_node = Node(value)
    new_node.right = self.head
    self.head = new_node

  def delete(self, value):
    if self.head is None:
      return
    if self.head.value == value:
      self.head = self.head.right
      return
    curr = self.head
    while curr.right is not None and curr.right.value != value:
      curr = curr.right
    if curr.right is not None:
      curr.right = curr.right.right

  def search(self, value):
    curr = self.head
    while curr is not None and curr.value != value:
      curr = curr.right
    return curr is not None
