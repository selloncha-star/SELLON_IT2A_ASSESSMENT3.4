from collections import deque


class TreeNode:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def build_sellon_tree():
  # Level 0 (Root)
  root = TreeNode("S")

  # Level 1
  root.left = TreeNode("E")
  root.right = TreeNode("L1")

  # Level 2
  root.left.left = TreeNode("L2")
  root.left.right = TreeNode("O")
  root.right.right = TreeNode("N")

  return root


def bfs_tree(root):
  if not root:
    return []

  result_list = []
  queue = deque([root])

  while queue:
    current = queue.popleft()
    result_list.append(current.value)

    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)

  return result_list


def dfs_tree_preorder(root):
  if not root:
    return []

  result_list = []
  stack = [root]

  while stack:
    current = stack.pop()
    result_list.append(current.value)

    # Push right child first so left child is processed first
    if current.right:
      stack.append(current.right)
    if current.left:
      stack.append(current.left)

  return result_list


if __name__ == "__main__":
  root_node = build_sellon_tree()

  bfs_res = bfs_tree(root_node)
  dfs_res = dfs_tree_preorder(root_node)

  print("=== Diagram 1: Binary Tree Traversal (SELLON) ===")
  print("BFS Result:", " - ".join(bfs_res))
  print("DFS Result:", " - ".join(dfs_res))