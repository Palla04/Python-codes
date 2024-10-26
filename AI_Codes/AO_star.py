class Node:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value  # Value for terminal nodes
        self.children = []  # Child nodes

def alpha_beta(node, depth, alpha, beta, maximizing_player):
    # Base case: if node is a terminal node or depth is zero
    if node.value is not None or depth == 0:
        return node.value

    if maximizing_player:
        max_eval = float('-inf')
        for child in node.children:
            eval = alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                print(f"Beta cut at node {node.name} with value {node.value} (alpha={alpha}, beta={beta})")
                break  # β cut
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.children:
            eval = alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                print(f"Alpha cut at node {node.name} with value {node.value} (alpha={alpha}, beta={beta})")
                break  # α cut
        return min_eval

def create_tree():
    root = Node('Root')

    num_children = int(input("Enter the number of children for the root node: "))
    
    for i in range(num_children):
        child_name = f'Child_{i}'
        child = Node(child_name)
        root.children.append(child)

        # Get number of grandchildren for this child
        num_grandchildren = int(input(f"Enter the number of grandchildren for {child_name}: "))
        for j in range(num_grandchildren):
            grandchild_name = f'Grandchild_{i}_{j}'
            grandchild = Node(grandchild_name)  # Create a child node

            # Get the number of leaf nodes for this grandchild
            num_leaves = int(input(f"Enter the number of leaf nodes for {grandchild_name}: "))
            for k in range(num_leaves):
                value = int(input(f"Enter the value for Leaf {grandchild_name}_{k}: "))
                leaf_node = Node(f'Leaf_{i}_{j}_{k}', value=value)
                grandchild.children.append(leaf_node)

            child.children.append(grandchild)

    return root

def main():
    # Create the game tree from user input
    root = create_tree()

    # Set initial values for alpha and beta
    alpha = float('-inf')
    beta = float('inf')

    # Perform Alpha-Beta pruning
    optimal_value = alpha_beta(root, depth=4, alpha=alpha, beta=beta, maximizing_player=True)

    print(f"Optimal value found: {optimal_value}")

if __name__ == "__main__":
    main()
