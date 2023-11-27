





class Node():
  def __init__(self, data):
    self.data = data
    self.next = None



class LinkedList:
  def __init__(self):
      self.head = None
  def insert_at_beginning(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
    else:
        new_node.next = self.head
        self.head = new_node
  def insertAtEnd(self, data):
      new_node = Node(data)
      if self.head is None:
          self.head = new_node
          return
  
      current_node = self.head
      while(current_node.next):
          current_node = current_node.next
  
      current_node.next = new_node



  def printLL(self):
    current_node = self.head
    while(current_node):
        print(current_node.data)
        current_node = current_node.next
 


llist = LinkedList()

llist.insertAtEnd('a')
llist.insertAtEnd('b')


llist.printLL()