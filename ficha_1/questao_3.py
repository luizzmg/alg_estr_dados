class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class Doubly_Linked_List:
  def __init__(self):
    self.start_node = None
    
  def ins_at_start(self, data):
    if self.start_node == None:
      self.start_node = Node(data)
      return 
    
    new_node = Node(data)
    
    new_node.next = self.start_node
    self.start_node = new_node
    new_node.next.prev = new_node

  def delete(self, data):
    if self.start_node.data == data:
      self.start_node = self.start_node.next
      
      if self.start_node: 
        self.start_node.prev = None
      
      return
    
    curr = self.start_node
    
    while curr.next != None:
      curr = curr.next
      
      if curr.data == data:
        if curr.prev: curr.prev.next = curr.next
        if curr.next: curr.next.prev = curr.prev
        return
  
  def move_to_start(self, data_node):
    self.delete(data_node)
    self.ins_at_start(data_node)
  
  def listed(self):
    if self.start_node == None: return []
    elements = []
    curr = self.start_node
    
    while curr != None:
      elements.append(curr.data)
      curr = curr.next
    
    return elements

# # # # # # # # # # # # # # # 

stories = Doubly_Linked_List()

entrada = input()

while entrada != "Mark fechou o instagram":
  nome = entrada.split(" ")[-1]
  comando = entrada.replace("Mark ","").replace(" " + nome,"")
  
  if comando == "seguiu":
    stories.ins_at_start(nome)
  
  elif comando == "deixou de seguir":
    stories.delete(nome)
  
  elif comando in ["curtiu o story de", "comentou no story de"]:
    stories.move_to_start(nome)

  entrada = input()

for pessoa in stories.listed():
  print(pessoa)
