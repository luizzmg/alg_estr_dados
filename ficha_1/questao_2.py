class Node:
  def __init__(self, data = None):
    self.data = data
    self.next = None

# # # # # # # # # # # # # #

# onde tiver "curr" vem de "current node"
# ou seja, nó atual

# alguns métodos nem precisava ter nessa questão
# mas fiz eles pra ver como estava indo a lista

# # # # # # # # # # # # # #

class Linked_list:
  def __init__(self):
    self.head = Node()
  
  def adding(self, data):
    new_node = Node(data)
    curr = self.head
    
    while curr.next != None:
      curr = curr.next
    
    curr.next = new_node
    
    print(f"Node {data} adicionado")
  
  def length(self):
    curr = self.head
    total = 0
    
    while curr.next != None:
      total += 1
      curr = curr.next
    
    return total

  def listed(self):
    elements = []
    curr = self.head
    
    while curr.next != None:
      curr = curr.next
      elements.append(curr.data)
    
    return elements
  
  def display(self):
    print(self.listed())
  
  def popping(self, index):
    last = self.head
    curr = last.next
    
    for _ in range(index):
      last = curr
      curr = last.next
    
    last.next = curr.next
  
  def find_index(self, node_data):
    curr = self.head
    i = 0
    
    while curr.next != None:
      curr = curr.next
      
      if curr.data == node_data:
        return i
      
      i += 1
    
    return None
  
  def find_node(self, node_data):
    curr = self.head
    
    while curr.next != None:
      curr = curr.next
      
      if curr.data == node_data:
        return curr
    
    return None
  
  def push(self, node_data):
    
    node = self.find_node(node_data)
    
    if node == None:
      print(f"Node {node_data} não existe")
    
    elif node.next == None:
      print(f"Não existe Node depois de {node_data}")
    
    else:
      back = self.head
      curr = back.next
      
      while curr.next != None:
        
        if curr == node:
          front = node.next
          node.next = front.next
          front.next = back.next
          back.next = front
          
          print(f"Node {node_data} empurrado")
          return
        
        back = curr
        curr = curr.next
  
  def pull(self, node_data):
    
    node_index = self.find_index(node_data)
    
    if node_index == None:
      print(f"Node {node_data} não existe")
    
    elif node_index == 0:
      print(f"Não existe Node antes de {node_data}")
    
    else:
      node = self.find_node(node_data)
      
      backs_back = self.head
      normal_back = backs_back.next
      curr = normal_back.next
      
      while backs_back.next != None:
        
        if curr == node:
          normal_back.next = node.next
          node.next = normal_back
          backs_back.next = node
          
          print(f"Node {node_data} puxado")
          return
        
        backs_back = normal_back
        normal_back = curr
        curr = curr.next

# # # # # # # # # # # # # #

listinha = Linked_list()

entrada = input()

while entrada != "fim!":
  entrada = entrada.split(":")
  node = entrada[0]
  cmd = entrada[1]
  
  if cmd == "adicione-me!":
    listinha.adding(node)
  
  elif cmd == "remova-me!":
    index = listinha.find_index(node)
    
    if index != None:
      print(f"Node {node} foi removido")
      listinha.popping(index)
    
    else:
      print(f"Node {node} não existe")
  
  elif cmd == "empurre-me!":
    listinha.push(node)
  
  elif cmd == "puxe-me!":
    listinha.pull(node)
  
  entrada = input()

lista_mapa = listinha.listed()

print("mapa:", end = "")
print(*lista_mapa, sep = "->")
