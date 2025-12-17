import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


heap = [0, 4, 1, 5, 10, 3]
nodes = [Node(value) for value in heap]

for i in range(len(heap)):
    left_index = 2 * i + 1
    right_index = 2 * i + 2

    print(f"\nТекущий узел: index={i}, value={nodes[i].val}")

    # проверяем левый ребёнок
    if left_index < len(heap):
        nodes[i].left = nodes[left_index]
        print(
            f"  Левый ребёнок существует: index={left_index}, value={nodes[left_index].val}"
        )
    else:
        print("  Левого ребёнка нет")

    # проверяем правый ребёнок
    if right_index < len(heap):
        nodes[i].right = nodes[right_index]
        print(
            f"  Правый ребёнок существует: index={right_index}, value={nodes[right_index].val}"
        )
    else:
        print("  Правого ребёнка нет")
