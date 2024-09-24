import heapq

def load_graph_data(graph_file):
    graph_map = {}
    file = open(graph_file, 'r')
    read_lines = file.readlines()
    file.close()

    for line in read_lines:
        split_line = line.strip().split()
        if len(split_line) > 1:
            current_city = split_line[0].lower()
            city_heuristic = int(split_line[1])
            graph_map[current_city] = {'heuristic': city_heuristic, 'neighbors': {}}
            for i in range(2, len(split_line), 2):
                adjacent_city = split_line[i].lower()
                city_distance = int(split_line[i+1])
                graph_map[current_city]['neighbors'][adjacent_city] = city_distance
        else:
            print(f"Ignoring line '{line}' due to unexpected format.")

    return graph_map

def a_star_shortest_path(graph_map, start_city, end_city):
    open_nodes = [(0, start_city)]
    path_history = {start_city: None}
    current_cost = {start_city: 0}

    while open_nodes:
        disValue, current_node = heapq.heappop(open_nodes)

        if current_node == end_city:
            break

        if current_node not in graph_map:
            print(f"Warning: Node '{current_node}' not found in the graph.")
            continue

        for adjacent_city, city_distance in graph_map[current_node]['neighbors'].items():
            updated_cost = current_cost[current_node] + city_distance
            if adjacent_city not in current_cost or updated_cost < current_cost[adjacent_city]:
                current_cost[adjacent_city] = updated_cost
                node_priority = updated_cost + graph_map[adjacent_city]['heuristic']
                heapq.heappush(open_nodes, (node_priority, adjacent_city))
                path_history[adjacent_city] = current_node

    return path_history, current_cost

def trace_back_path(path_history, start_city, end_city):
    current_node = end_city
    path_list = []
    while current_node!= start_city:
        if current_node in path_history:
            path_list.append(current_node)
            current_node = path_history[current_node]
        else:
            break
    path_list.append(start_city)
    path_list.reverse()
    return path_list

graph_file = "21301559_NafisRayan_CSE422_09_Lab_Assignment01_InputFile_Summer2024.txt"
graph_map = load_graph_data(graph_file)

start_city = input("Start node: ").lower()
end_city = input("Destination: ").lower()

path_history, costValue = a_star_shortest_path(graph_map, start_city, end_city)
path_list = trace_back_path(path_history, start_city, end_city)

if path_list:
  printPath=path_list.copy()
  for i in range(len(printPath)):
    printPath[i] = printPath[i].capitalize()

  print(f"Path: {' -> '.join(printPath)}")
  total_distance = 0
  for i in range(len(path_list) - 1):
      current_node = path_list[i]
      next_node = path_list[i + 1]
      if current_node in graph_map[next_node]['neighbors']:
          total_distance += graph_map[next_node]['neighbors'][current_node]
      else:
          print(f"Warning: No direct connection found between {next_node} and {current_node}.")
  print(f"Total distance: {total_distance} km")
else:
  print("NO PATH FOUND")
