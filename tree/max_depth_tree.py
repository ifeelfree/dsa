
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def max_depth_recursive(root):
    # Base case: empty tree has depth -1
    if root is None:
        return -1
    # Recursive case: 1 + maximum of left and right subtree depths
    left_depth = max_depth_recursive(root.left)
    right_depth = max_depth_recursive(root.right)

    return 1 + max(left_depth, right_depth)

def max_depth_bfs(root):
    if not root:
        return -1
    from collections import deque
    queue = deque([root])
    depth = -1
    while queue:
        depth += 1

        # process all nodes at current level
        level_len = len(queue)
        for _ in range(level_len):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return depth


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(max_depth_recursive(root))
    print(max_depth_bfs(root))