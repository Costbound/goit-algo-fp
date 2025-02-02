import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="#00008B"):  # Default color set to dark blue
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

def heap_to_tree(heap):
    if not heap:
        return None

    nodes = [Node(key) for key in heap]
    for i in range(len(heap)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(heap):
            nodes[i].left = nodes[left_index]
        if right_index < len(heap):
            nodes[i].right = nodes[right_index]
    return nodes[0]

def generate_color(index):
    """Generate a color from dark blue to light blue based on the index."""
    blue_intensity = min(255, 150 + index * 20)  # Start from 50 and increment by 20
    return f'#0000{blue_intensity:02x}'

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def depth_first_traversal(root, colors):
    if root is None:
        return
    stack = [root]
    index = 0
    while stack:
        node = stack.pop()
        node.color = generate_color(index)
        colors.append(node.color)
        index += 1
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def breadth_first_traversal(root, colors):
    if root is None:
        return
    queue = deque([root])
    index = 0
    while queue:
        node = queue.popleft()
        node.color = generate_color(index)
        colors.append(node.color)
        index += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Example binary heap
heap = [0, 4, 1, 5, 10, 3]

# Convert heap to binary tree
root = heap_to_tree(heap)

# Count total nodes
total_nodes = count_nodes(root)

# Visualize depth-first traversal
colors = []
depth_first_traversal(root, colors)
print("Depth-First Traversal Colors:", colors)
draw_tree(root)

# Reset colors for breadth-first traversal
root = heap_to_tree(heap)
colors = []
breadth_first_traversal(root, colors)
print("Breadth-First Traversal Colors:", colors)
draw_tree(root)