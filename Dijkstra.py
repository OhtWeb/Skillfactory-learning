from collections import defaultdict


def dijkstra(graph, source):
    distances = defaultdict(lambda: float('inf'))  
    previous = {}  
    unvisited = set(graph.keys()) 

    distances[source] = 0  

    while unvisited:  # Пока есть непосещенные вершины
        current_node = min(unvisited, key=lambda node: distances.get(node, float(
            'inf'))) 
        unvisited.remove(current_node)  

        # Финальная часть алгоритма:
        for neighbor, weight in graph[current_node].items():  
            new_distance = distances[current_node] + weight 
            if new_distance < distances[neighbor]:  
                distances[neighbor] = new_distance 
                previous[
                    neighbor] = current_node 

    return distances, previous

def get_shortest_path(previous, source, target):
    path = [target]  # Начинаем с целевой вершины
    while path[-1] != source:  # Пока не достигнем начальной вершины
        path.append(previous[path[-1]])  # Добавляем предыдущую вершину на путь к текущей вершине
    path.reverse()  # Переворачиваем список, чтобы путь был от начальной вершины к целевой
    return path

weighted_graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'D': 4, 'E': 3},
    'C': {'A': 2, 'F': 7},
    'D': {'B': 4},
    'E': {'B': 3, 'F': 6},
    'F': {'C': 7, 'E': 6}
}

# Находим кратчайшие пути от узла 'D'
distances, previous = dijkstra(weighted_graph, 'D')
# Выводим кратчайший путь от 'D' до 'F'
path = get_shortest_path(previous, 'D', 'F')
print(f"Кратчайший путь от D до F: {path}")
# Кратчайший путь от D до F: ['D', 'B', 'E', 'F']