from collections import deque

# Adjacency list representation for Diagram 2: Graph (SELLON)
graph = {
    "S": ["E", "L1"],
    "E": ["S", "L2", "O"],
    "L1": ["S", "O", "N"],
    "L2": ["E", "O"],
    "O": ["E", "L1", "L2", "N"],
    "N": ["L1", "O"],
}


def bfs_graph(adj_list, start_vertex):
  visited_list = []
  seen = {start_vertex}
  queue = deque([start_vertex])

  while queue:
    current = queue.popleft()
    visited_list.append(current)

    for neighbor in adj_list[current]:
      if neighbor not in seen:
        seen.add(neighbor)
        queue.append(neighbor)

  return visited_list


def dfs_graph(adj_list, start_vertex):
  visited_list = []
  seen = set()
  stack = [start_vertex]

  while stack:
    current = stack.pop()
    if current not in seen:
      seen.add(current)
      visited_list.append(current)

      # Push neighbors in reverse order to explore leftmost first
      for neighbor in reversed(adj_list[current]):
        if neighbor not in seen:
          stack.append(neighbor)

  return visited_list


if __name__ == "__main__":
  start_node = "S"

  bfs_res = bfs_graph(graph, start_node)
  dfs_res = dfs_graph(graph, start_node)

  print("=== Diagram 2: Graph Traversal (SELLON) ===")
  print("BFS Result:", " - ".join(bfs_res))
  print("DFS Result:", " - ".join(dfs_res))