import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
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
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def dfs(root):
    stack = [root]
    order = []
    while stack:
        node = stack.pop()
        if node:
            order.append(node)
            stack.append(node.right)
            stack.append(node.left)
    return order

def bfs(root):
    queue = [root]
    order = []
    while queue:
        node = queue.pop(0)
        if node:
            order.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return order


def update_colors(order):
    n = len(order)
    for i, node in enumerate(order):
        intensity = int(255 * i / (n - 1))
        hex_intensity = f'{intensity:02x}'
        node.color = f'#{hex_intensity}ff{hex_intensity}'


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Обхід в глибину (DFS)
dfs_order = dfs(root)
update_colors(dfs_order)
draw_tree(root)

# Обхід в ширину (BFS)
bfs_order = bfs(root)
update_colors(bfs_order)
draw_tree(root)
