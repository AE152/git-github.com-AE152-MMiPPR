import networkx as nx

# Данные из таблицы
jobs = [
    (0, 1, 6),  # (Начало, Конец, Длительность)
    (0, 2, 3),
    (0, 3, 7),
    (1, 4, 10),
    (2, 5, 8),
    (2, 6, 5),
    (3, 6, 6),
    (4, 5, 9),
    (4, 7, 4),
    (5, 8, 3),
    (5, 9, 5),
    (6, 8, 7),
    (7, 9, 2),
    (8, 9, 6),
    (9, 10, 2),
]

# Создание направленного графа
G = nx.DiGraph()
for start, end, duration in jobs:
    G.add_edge(start, end, weight=duration)

# Вычисление ранних сроков
early_times = {node: 0 for node in G.nodes()}
for node in nx.topological_sort(G):
    for pred in G.predecessors(node):
        early_times[node] = max(early_times[node], 
                                early_times[pred] + G[pred][node]['weight'])

# Вычисление поздних сроков
late_times = {node: max(early_times.values()) for node in G.nodes()}
for node in reversed(list(nx.topological_sort(G))):
    for succ in G.successors(node):
        late_times[node] = min(late_times[node], 
                               late_times[succ] - G[node][succ]['weight'])

# Резервы времени и критический путь
reserves = {}
critical_path = []
for start, end in G.edges():
    duration = G[start][end]['weight']
    reserve = late_times[end] - early_times[start] - duration
    reserves[(start, end)] = reserve
    if reserve == 0:
        critical_path.append((start, end))

# Вывод результатов
print("Ранние сроки: ", early_times)
print("Поздние сроки: ", late_times)
print("Резервы времени: ", reserves)
print("Критический путь: ", critical_path)
