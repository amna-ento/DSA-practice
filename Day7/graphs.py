#  graph
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

vertices = list(graph.keys())
edges = sum(len(neighbors) for neighbors in graph.values()) // 2

print("Vertices:", vertices)
print("Edges:", edges)


#adjancy graph
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

print(graph)

#grapg traversal
def traverse(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

traverse(graph, "A")


#dfs
def dfs(graph, start):
    visited = set()
    order = []

    def visit(node):
        if node in visited:
            return
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            visit(neighbor)

    visit(start)
    return order

print(dfs(graph, "A"))


#binary tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.right = Node(20)

print("Root:", root.value)
print("Leaf nodes:", [2, 7, 20])  # example values
print("Children of 5:", root.left.left.value, root.left.right.value)


#tree traversal
def preorder(node):
    if node is None:
        return
    print(node.value, end=" ")
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.value, end=" ")
    inorder(node.right)

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value, end=" ")

print("Preorder:")
preorder(root)
print("\nInorder:")
inorder(root)
print("\nPostorder:")
postorder(root)