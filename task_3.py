import heapq
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict, deque

def dijkstra(graph, start):
    # Ініціалізація
    pq = []  # Пріоритетна черга (бінарна купа)
    heapq.heappush(pq, (0, start))
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    shortest_paths = {node: [] for node in graph}
    shortest_paths[start] = [start]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                shortest_paths[neighbor] = shortest_paths[current_node] + [neighbor]

    return distances, shortest_paths

# Створення графа
G = nx.Graph()
G.add_weighted_edges_from([("Hanna", "Dmytro", 3), ("Hanna", "Viki", 2), ("Hanna", "Mariia", 5),
                           ("Dmytro", "Viki", 1), ("Dmytro", "Mykhailo", 4), ("Roman", "Viki", 2),
                           ("Viki", "Dmytro", 1), ("Hanna", "Roman", 3)])

# Перетворення в формат для алгоритму Дейкстри
graph = defaultdict(dict)
for u, v, data in G.edges(data=True):
    weight = data['weight']
    graph[u][v] = weight
    graph[v][u] = weight  # Якщо граф не орієнтований

# Виконання алгоритму Дейкстри
start_node = "Hanna"
distances, shortest_paths = dijkstra(graph, start_node)

# Виведення результатів
print(f"Довжини найкоротших шляхів: {distances}")
print(f"Найкоротші шляхи від {start_node} до інших вершин:")
for node in shortest_paths:
    print(f"{start_node} -> {node}: {' -> '.join(shortest_paths[node])}")

# Візуалізація графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=10, font_weight='bold', edge_color='gray')
edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True) if 'weight' in d}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Соціальна мережа")
plt.show()
