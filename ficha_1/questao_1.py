"""
Estou refazendo o código
agora implementando de fato
uma pilha, da mesma forma
como foi mostrada na questão
do dia 20/11/23
"""

class Node:
  def __init__(self, data):
    self.data = data
    self.next_node = None

class Stack:
  def __init__(self):
    self.top = None

  def is_empty(self):
    return self.top is None

  def push(self, data):
    node = Node(data)
    node.next_node = self.top
    self.top = node

  def pop(self):
    if self.is_empty():
      return None
    
    element_pop = self.top.data
    self.top = self.top.next_node
    return element_pop

  def get(self):
    current = self.top
    elements = []
    
    while current:
      elements.append(current.data)
      current = current.next_node
      
    return elements

# Daqui pra frente vou fazer em português. Cansei.

#################################################

def verificar_ordem(lista):
  
  representacoes = {
    "endrick": "new balance", 
    "neymar" : "puma", 
    "cr7"    : "nike", 
    "messi"  : "adidas"}
  
  marcas_pode, marcas_falta = [], 0
  
  for item in lista:
    if item in representacoes.values(): # é marca
      
      if item in marcas_pode:
        marcas_pode.remove(item)
        marcas_falta -= 1
      
      else:
        marcas_falta += 1
      
    if item in representacoes.keys(): # é jogador
      marcas_pode.append(representacoes[item])
      marcas_falta += 1
  
  if marcas_falta == 0: return True
  else: return False

############################

entrada = input().split("-")

pilha = Stack()

for coisa in entrada:
  pilha.push(coisa)

nova = pilha.get()
nova.reverse()

if verificar_ordem(nova):
  print("Correto")

else:
  print("Incorreto")
