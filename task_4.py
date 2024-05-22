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

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def heapify(arr, n, i):
    largest = i  # Ініціалізуємо найбільший як корінь
    left = 2 * i + 1  # лівий = 2*i + 1
    right = 2 * i + 2  # правий = 2*i + 2

    # Перевіряємо чи лівий нащадок існує і чи він більший за корінь
    if left < n and arr[i] < arr[left]:
        largest = left

    # Перевіряємо чи правий нащадок існує і чи він більший за найбільший на даний момент
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Заміна кореня, якщо необхідно
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # обмін
        heapify(arr, n, largest)  # рекурсивно heapify піддерево

def build_heap(arr):
    n = len(arr)
    # Починаємо з останнього не листового вузла і застосовуємо heapify до кожного
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def array_to_bst(arr, root, i, n):
    if i < n:
        temp = Node(arr[i])
        root = temp

        root.left = array_to_bst(arr, root.left, 2 * i + 1, n)
        root.right = array_to_bst(arr, root.right, 2 * i + 2, n)

    return root

def visualize_heap(arr):
    build_heap(arr)  # Перетворюємо масив у купу
    n = len(arr)
    root = array_to_bst(arr, None, 0, n)
    draw_tree(root)

# Приклад використання
heap_array = [3, 9, 5, 6, 8, 20, 10]
visualize_heap(heap_array)
