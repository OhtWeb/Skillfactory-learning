class Node:
   def __init__(self, value, children=None):
       self.value = value
       self.children = children if children else []
root = Node(5, [
   Node(3, [
       Node(1),
       Node(4)
   ]),
   Node(2, [
       Node(6),
       Node(-1)
   ])
])
print(root.value)
# 5
# Получение значений дочерних узлов
print(root.children[0].value, root.children[1].value)
# 3 2
# Получение значений листьев
print(root.children[0].children[0].value, root.children[0].children[1].value)
print(root.children[1].children[0].value, root.children[1].children[1].value)
# 1 4
# 6 -1